import datetime

from flask import Flask, render_template, redirect
import blog

app = Flask(__name__)
blog_app = blog.create_app(config)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/index')
def index():
    redirect('/blog')

@app.route('/blog')
def blog():
    return redirect('blog.html')

@app.route('/create')
def create():
    return render_template('create.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
