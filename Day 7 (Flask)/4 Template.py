from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    greet = '<h1>Hello, Students of VVIET College</h1>'
    link = '<p><a href="user/Nishanth">Click me</a></h1>'
    return greet + link


@app.route('/<name>')
def username(name):
    personal = f'<h1>Hello, {name}!</h1>'
    return personal


@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'

    instruc = f'<p>Mr {name} Check the name in the <strong>browser address bar</strong>  and reload the page.</p>'
    return personal + instruc


if __name__ == '__main__':
    app.run(debug = True)
