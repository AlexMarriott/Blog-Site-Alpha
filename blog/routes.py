from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from flask_login import login_required,current_user
from google.cloud import storage

from .forms import PostForm, Comment
from API.common import get_model, check_post_author
from API import storage

"""
The blog blueprint handles all of the processing for the comments and post. It will past the write/read requests to the model_datastore
to handle and connect to the googledatastore.
"""
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
@login_required
def add_comment(id):
    form = Comment()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        comment_time = datetime.now().timestamp()
            #datetime.now().replace(second=0, microsecond=0)
        sql_data = {'commenter': current_user.name, 'comment': data['comment'], 'timestamp': comment_time}
        get_model().create(sql_data, id=id, kind='Comment')

    return redirect(url_for('blog.view_post', id=id))

@blog.route('/blog/edit_comment', methods=['GET', 'POST'])
@login_required
def edit_comment():
    pass

@blog.route('/blog/delete_comment', methods=['POST'])
@login_required
def delete_comment():
    pass


@blog.route('/blog/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        data['author'] = current_user.name
        image = ''
        post_time = datetime.now().timestamp()
        try:
            image = file_upload(request.files.get('file'))
            if not image:
                image = 'https://storage.cloud.google.com/badgcloudstorage/pusheen-2019-12-10-233107.jpg'
        except Exception as e:
            print('Could not upload file, something went wrong error is:{0}'.format(e))

        sql_data = {'title': data['title'],
                    'content': data['post_data'],
                    'author': current_user.name,
                    'author_id': current_user.id,
                    'timestamp': post_time,
                    'picture_url': image}
        post = get_model().create(sql_data)

        return redirect(url_for('blog.view_post', id=post['id']))
    else:
        try:
            flash(form.errors["post_data"][0], 'warning')
        except KeyError:
            pass
    return render_template("form.html", action='blog.create_post', post={}, form=form)

@blog.route('/blog/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    form = PostForm()
    post = get_model().from_datastore(get_model().read(id, 'Post'))

    if not check_post_author(post['author_id'], current_user.id):
        flash('Only the owner of the post can edit it that post', 'warning')
        return redirect(url_for('blog.view_post', id=post['id']))

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        post_time = datetime.now().timestamp()
            #datetime.now().replace(second=0, microsecond=0)
        try:
            file = file_upload(request.files.get('file'))
            if not file:
                file = post['picture_url']
        except Exception as e:
            print('Could not upload file, something went wrong error is:{0}'.format(e))
        sql_data = {'title': data['title'], 'content': data['post_data'], 'author': current_user.name, 'author_id': current_user.id, 'updated_timestamp': post_time,'timestamp':post['timestamp'], 'picture_url': file}

        post = get_model().update(sql_data, id=id)
        return redirect(url_for('blog.view_post', id=post['id']))

    return render_template("form.html", action='blog.edit_post', post=post, id=post['id'], form=form)

@blog.route('/blog/delete/<id>')
@login_required
def delete_post(id):
    get_model().delete(id)
    render_template(redirect(url_for('blog.blog')))


def file_upload(file):
    """
        Upload the user-uploaded file to Google Cloud Storage and retrieve its
        publicly-accessible URL.
        """
    if not file or isinstance(file, str):
        return False

    public_url = storage.upload_file(file.read(),
        file.filename,
        file.content_type)

    current_app.logger.info(
        "Uploaded file %s as %s.", file.filename, public_url)

    print("Uploaded file %s as %s.", file.filename, public_url)

    return public_url
