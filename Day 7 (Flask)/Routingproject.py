from flask import Flask

app = Flask(__name__)

@app.route('/home/')
def home():
    return "Hello, Welcome to our website with routing"

if __name__ == "__main__":
    app.run(debug=True)