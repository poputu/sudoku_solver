from flask import render_template, request, flash

from app import app
from . import sudoky


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sudoku1 = [request.form.getlist('row0', type=int), request.form.getlist('row1', type=int),
                   request.form.getlist('row2', type=int),
                   request.form.getlist('row3', type=int), request.form.getlist('row4', type=int),
                   request.form.getlist('row5', type=int),
                   request.form.getlist('row6', type=int), request.form.getlist('row7', type=int),
                   request.form.getlist('row8', type=int)]
        if sudoky.checkifsudoku(sudoku1):
            sudoky.solveSudoku(sudoku1)
        else:
            flash('This sudoku is invalid, please enter sudoku with right values')

        return render_template("return.html", sudoku1=sudoku1)

    return render_template("index.html")
