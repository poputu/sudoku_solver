from app import app
from flask import render_template, request
from tabulate import tabulate
from . import sudoky

def error1():
    return render_template("index.html", text='this sudoku is not valid')

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sudoku1 = [request.form.getlist('row0', type=int),request.form.getlist('row1', type=int),request.form.getlist('row2', type=int),
                  request.form.getlist('row3', type=int),request.form.getlist('row4', type=int),request.form.getlist('row5', type=int), 
                  request.form.getlist('row6', type=int),request.form.getlist('row7', type=int),request.form.getlist('row8', type=int)]

        sudoky.solveSudoku(sudoku1)
        #return tabulate(sudoku1, tablefmt='html')
        return render_template("return.html", sudoku1 = sudoku1)
        #return render_template("return.html", sudoku1 = sudoku1)
        
    return render_template("index.html")