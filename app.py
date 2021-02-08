from flask import Flask
from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLAlchemy＿DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
app.debug = True
main = Blueprint('main', __name__)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    comment_text = db.Column(db.String(1000))

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')
    return f'Name: {name}, Comment: {comment}'

app.register_blueprint(main)
if __name__=='__main__':
    app.run(debug=True)