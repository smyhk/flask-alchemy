from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
