from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def landing():
    return "<a href = '/vote'> Vote here </a>"

#decorator
@app.route('/vote', methods = ['GET', 'POST']) #http://127:0.0.1:5000/vote
def vote():
    if request.method == 'POST':
        name = request.form.get("f_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        choice = request.form.get("party")
        comment = request.form.get("comment")
        data = [name, age, gender, choice, comment]
        return render_template("output.html", data = data)
    if request.method == 'GET':
        return render_template("input.html")



app.run()

#tkinter - embedded application (installed apps)
#app.loop()

#step2
#step deploy application 
#define domain
#define security https

