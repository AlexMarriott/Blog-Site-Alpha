from flask import Flask
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient

import config
from API.model_datastore import get_user


def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login_manager = LoginManager()
    login_manager.init_app(app)

    #Register the blueprints
    from auth.routes import auth
    from blog.routes import blog
    from main.routes import main
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(main)

    @login_manager.user_loader
    def load_user(user_id):
        return get_user(user_id)

    return app



application = create_app(config)

if __name__ == '__main__':
    application .run(host='0.0.0.0', port='8080',  debug=True, ssl_context="adhoc")
