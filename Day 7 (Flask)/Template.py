from flask import *
app = Flask(__name__)

@app.route('/')
def about():
    return "<html><body><h1>Hi, Welcome to the website</h1></body></html>"

if __name__ == '__main__':
    app.run(debug = True)