from flask import Flask, render_template
import requests
from post import Post
import datetime

current_year = datetime.date.today().year
posts = requests.get('https://api.npoint.io/dba21db358a3ffda830f').json()
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'],post['body'])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts = post_objects, year=current_year)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, year=current_year)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)