from flask import Flask, render_template, request
import smtplib,ssl
import requests
import datetime
from keys import MY_EMAIL, MY_PASSWORD

current_year = datetime.date.today().year
posts = requests.get('https://api.npoint.io/e85468e122a65f59873b').json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts, year=current_year)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, year=current_year)

@app.route('/about')
def about():
    return render_template('about.html',year=current_year)


@app.route("/contact", methods=["GET", "POST"])

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs="iamsdawson@gmail.com", 
        msg=email_message
        )
    
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0',debug=True)
