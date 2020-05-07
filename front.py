from flask import Flask, request, render_template, redirect, url_for
import pgcon
app = Flask(__name__, template_folder = './templates/')

d = pgcon.DBC()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/update', methods=['GET', 'POST']) #allow both GET and POST requests
def update():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        nameval = request.form.get('name')
        matchval = request.form.get('matches')
        goalval = request.form.get('goals')
        assistval = request.form.get('assists')
        if not nameval or not matchval or not goalval or not assistval:
            return 'Incomplete information, please post request again and enter information properly.'
        d.addToDB(nameval, matchval, goalval, assistval)
        rows = d.displayDB()
        print(rows)
        return render_template('display.html', data=rows)

    return render_template('retpage.html')

@app.route('/display', methods=['GET','POST'])
def display():
    rows = d.displayDB()
    print(rows)
    return render_template('display.html', data=rows)

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        nameval = request.form.get('name')
        if not nameval: return 'Incomplete information, please post request again and enter information properly.'
        d.deleteFromDB(nameval)
        rows = d.displayDB()
        print(rows)
        return render_template('display.html', data=rows)
    return ''' <form method="POST">
                Name: <input type="text" name="name"><br>
                <input type="submit" value="Submit"><br>
            </form> '''

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if 'update' in request.form:
            return redirect(url_for('update'))
        if 'delete' in request.form:
            return redirect(url_for('delete'))
        if 'display' in request.form:
            return redirect(url_for('display'))
    return '''  <form method="POST"
                <input type="submit" name="update" value="Update">
                <input type="submit" name="delete" value="Delete"> 
                <input type="submit" name="display" value="Display"> 
                </form> '''

if __name__ == '__main__':
    app.run(debug=True,port=5000)