
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods= ['POST'])
def process():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')


@app.route('/result')
def results():
    return render_template('result.html', dojo = Dojo.get_one())

