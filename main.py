from flask import Flask, render_template
import requests
import datetime

current_year = datetime.date.today().year
posts = requests.get('https://api.npoint.io/e85468e122a65f59873b').json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts = posts, year=current_year)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, year=current_year)

@app.route('/about')
def about():
    return render_template('about.html',year=current_year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=current_year)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)