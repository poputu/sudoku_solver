from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SudokuForm(FlaskForm):
    row0 = StringField('row0')
    row1 = StringField('row1')
    row2 = StringField('row2')
    row3 = StringField('row3')
    row4 = StringField('row4')
    row5 = StringField('row5')
    row6 = StringField('row6')
    row7 = StringField('row7')
    row8 = StringField('row8')
    submit = SubmitField('solve sudoku')