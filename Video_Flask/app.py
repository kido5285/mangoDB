from flask import Flask
from flask import Blueprint, render_template
app = Flask(__name__)
app.debug = True
main = Blueprint('main', __name__)
@app.route('/')
def create_app():
    return render_template('index.html')

@main.route('/sign')
def sign():
    return 'sign page'

if __name__=='__main__':
    app.run(debug=True)