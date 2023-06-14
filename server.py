from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'This is the blog page!'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is from 2020 about my dogs!'
