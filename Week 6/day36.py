# What is Flask?
# Setting Up Flask
# Creating Your First Flask Route
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def  hello():
#     return "Hello, Flask!"

# if __name__ == '__main__':
#     app.run(debug=True)

# Understanding Flask Templates

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def  hello():
#     return render_template('index.html', name='Flask Developer')

# if __name__ == '__main__':
#     app.run(debug=True)

# Day 36 Project: Hello Flask App

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)
    
    