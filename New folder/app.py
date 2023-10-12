from flask import Flask, request, render_template, redirect 

app = Flask(__name__)

@app.route('/')
def landing():
    return "<a href='/vote'>Vote here</a>"

@app.route('/vote', methods = ['GET','POST'])   # http://127.0.0.1:5000/vote 
def vote():
    if request.method == 'POST':
        name = request.form.get("f_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        choice = request.form.get("party")
        comment = request.form.get("comment")
        data = [name, age, gender, choice, comment]
        # return render_template("output.html", data = data)
        return "<h1>Form Submitted!</h1>"
    if request.method == 'GET':
        return render_template("input.html")

app.run()






















# @app.route('/Main_Page') #http://127.0.0.1:5000/Main_Page
# def hello_in_english()


app.run()

# step deploy application
# define domain
# define security https

# https://www.wikipedia.org/
# https://www.wikipedia.org/Main_Page

