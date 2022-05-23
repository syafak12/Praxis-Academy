from flask import Flask
from markupsafe import escape
app = Flask
@app.route('/user/<username>')
def show_user_profile(username):
    # tampilkan profil pengguna untuk pengguna itu
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # tampilkan postingan dengan id yang diberikan, id adalah bilangan bulat
    return 'Post %d' % post_id

@app.route('.path/<path:subpath>')
def show_subpath(subpath):
    # tampilkan subpath setelah /path/
    return 'subpath %d' % escape(subpath)