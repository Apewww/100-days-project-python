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
