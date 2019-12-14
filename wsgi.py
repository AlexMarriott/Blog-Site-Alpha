import time
import config

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from API.model_datastore import get_user

def create_app(config_class=config):
    """
    Load the information within the config file along with defining the login manager to help with users sessions.
    :param config_class:
    :return: app
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    login_manager = LoginManager()
    login_manager.init_app(app)

    #Register the blueprints
    from auth.routes import auth
    from blog.routes import blog
    from main.routes import main
    from trello_card.routes import trello_card
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(trello_card)
    app.register_blueprint(main)


    @login_manager.user_loader
    def load_user(user_id):
        try:
            return get_user(user_id)
        except Exception:
            return None

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('auth.login'))

    @app.template_filter('ctime')
    def timectime(s):
        return time.ctime(s)
    return app

app = create_app(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', ssl_context='adhoc')
