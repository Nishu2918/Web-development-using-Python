from flask import Flask
app = Flask(__name__)

@app.route('/<age>')
def user(age):
    greet = '<h1>Hello, Students of VVIET College</h1>'
    link = f'<h2>My name is Nishanth, My age is {age}</h2>'
    return greet + link

if __name__ == '__main__':
    app.run(debug=True)