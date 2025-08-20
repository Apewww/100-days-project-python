from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [
        {"id": 1, "title": "First Post", "content": "This is my first blog post."},
        {"id": 2, "title": "Second Post", "content": "Another day, another post."},
        {"id": 3, "title": "Third Post", "content": "Awesome Post."}
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
