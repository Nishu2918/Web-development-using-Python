from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('flipkart.html')

# @app.route('/kannada')
# def kannada():
#     return render_template('kannada.html')

if __name__ == '__main__':
    app.run(debug=True)