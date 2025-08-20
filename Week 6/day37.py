# Advanced Flask Routing
# from flask import Flask

# app = Flask(__name__)

# @app.route('/home')
# def home():
#     return "Welcome to My Blog!"
    
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f"Displaying Post #{post_id}"   
    
# if __name__ == '__main__':
#     app.run(debug=True)
    
# Dynamic Templates with Jinja2
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/home')
# def home():
#     return render_template('index37.html', title="Welcome to My Blox")
    
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f"Displaying Post #{post_id}"   
    
# if __name__ == '__main__':
#     app.run(debug=True)

# Passing Data Between Routes and Templates
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     posts = [
#         {"id": 1, "title": "First Post", "content": "First Content"},
#         {"id": 2, "title": "Second Post", "content": "Second Content"},
#     ]

#     return render_template('index37_2.html', posts=posts)
    
# if __name__ == '__main__':
#     app.run(debug=True)
# Organizing Flask Projects for Scalability
# Day 37 Project: Personal Blog Website