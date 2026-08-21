#sample commit1
#sample commit 2
#sample commit 3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/health')
def health():
    return 'Server is up and running'
