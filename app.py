from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/skedzie/Development/flaskalchemy/blog.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    sub_title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    blogpost = BlogPost.query.filter_by(id=post_id).one()

    date = blogpost.date_posted.strftime('%B %d, %Y')

    return render_template("post.html", post=blogpost, date_posted=date)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/addpost")
def add_post():
    return render_template("addpost.html")


@app.route("/publishpost", methods=['POST'])
def publish():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    blogpost = BlogPost(title=title, sub_title=subtitle, author=author, content=content, date_posted=datetime.now())
    db.session.add(blogpost)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
