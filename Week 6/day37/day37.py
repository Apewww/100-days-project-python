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
from flask import Flask, render_template

app = Flask(__name__)

# Sample Blog Posts
posts = [
    {"id": 1, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 2, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
    {"id": 3, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 4, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
    {"id": 5, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 6, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
    {"id": 7, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 8, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
    {"id": 9, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 10, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
    {"id": 11, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 12, "title": "Advanced Flask Routing", "content": "Understand dynamic routes.", "author": "Bob"},
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "<h1>Post Not Found</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)
