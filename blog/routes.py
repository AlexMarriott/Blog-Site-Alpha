import datetime

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .forms import PostForm, Comment
from API.common import get_model
dt = datetime.datetime.now()

blog = Blueprint('blog', __name__)
@blog.route('/blog')
def blog_index():
    posts = get_model().list()
    return render_template('blog.html', posts=posts)

@blog.route('/blog/view/<id>')
def view_post(id):
    form = Comment()
    post = get_model().read(id, 'Post')
    comments = get_model().read(id, 'Comment')
    return render_template('post.html', action='blog.add_comment',post=post, comments=comments, form=form)

@blog.route('/blog/add_comment/<id>', methods=['GET', 'POST'])
def add_comment(id):
    form = Comment()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        comment_time = datetime.date(dt.year, dt.month, dt.day)
        sql_data = {'comment': data['comment'], 'commenter': 'alex', 'timestamp': str(comment_time)}
        get_model().create(sql_data, id=id, kind='Comment')

    return redirect(url_for('blog.view_post', id=id))

@blog.route('/blog/edit_comment', methods=['GET', 'POST'])
def edit_comment():
    pass

@blog.route('/blog/delete_comment', methods=['POST'])
def delete_comment():
    pass


@login_required
@blog.route('/blog/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        data['author'] = 'alex'
        post_time = datetime.date(dt.year, dt.month, dt.day)
        sql_data = {'title': data['title'], 'content': data['post_data'], 'author': 'alex', 'timestamp':str(post_time)}
        post = get_model().create(sql_data)

        return redirect(url_for('blog.view_post', id=post['id']))

    return render_template("form.html", action='blog.create_post', post={}, form=form)

@blog.route('/blog/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    form = PostForm()
    post = get_model().read(id, 'Post')
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        post_time = datetime.date(dt.year, dt.month, dt.day)
        sql_data = {'title': data['title'], 'content': data['post_data'], 'author': 'alex', 'timestamp':str(post_time)}

        post = get_model().update(sql_data, id=id)
        return redirect(url_for('blog.view_post', id=post['id']))

    return render_template("form.html", action='blog.edit_post', post=post, id=post['id'], form=form)

@blog.route('/blog/delete/<id>')
def delete_post(id):
    get_model().delete(id)

    render_template(redirect(url_for('blog.blog')))
