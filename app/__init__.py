from flask import Flask




app = Flask(__name__)

app.config['SECRET_KEY'] = "some_random_stuff_plus"


from app import routes