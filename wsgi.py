from flask import Flask
import config

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from blog.routes import blog
    from main.routes import main
    app.register_blueprint(blog)
    app.register_blueprint(main)
    return app


application = create_app()

if __name__ == '__main__':
    application .run(host='0.0.0.0', port='8080',  debug=True)
