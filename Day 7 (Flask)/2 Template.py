from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greet = '<h1>Hello, Students of VVIET College</h1>'
    link = '<p><a href="user/Nishanth">Click me</a></h1>'
    return greet + link


if __name__ == '__main__':
    app.run(debug = True)