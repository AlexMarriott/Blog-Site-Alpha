from flask import Blueprint, render_template, request, redirect, url_for

from API.common import get_model

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blog_index():
    return render_template('blog.html')

@blog.route('/blog/view/<id>')
def view_post(id):
    pass

@blog.route('/blog/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        blog = get_model().create(data)

        return redirect(url_for('.view', id=blog['id']))

    return render_template("form.html", action="Add", blog={})

@blog.route('/blog/edit/<id>')
def edit_post(id):
    pass
@blog.route('/blog/delete/<id>')
def delete_post(id):
    pass