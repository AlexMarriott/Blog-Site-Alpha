from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('index.html')

@main.route('/index')
def index():
    return redirect(url_for('main.root'))

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')