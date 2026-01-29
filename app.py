from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def blog_home():
    posts = [
        {
            "title": "My First Blog",
            "content": "This is my first Flask blog post.",
            "author": "Bishnu"
        },
        {
            "title": "Why I am learning Flask",
            "content": "Flask is simple, powerful and perfect for small projects.",
            "author": "Bishnu"
        }
    ]
    return render_template("blog/index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

