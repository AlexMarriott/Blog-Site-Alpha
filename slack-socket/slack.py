from flask import current_app, render_template
from flask_socketio import SocketIO
from flask import Blueprint, Flask

import config

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app

application = create_app()
socketio = SocketIO(application)

@application.route('/api')
def test():
    return render_template('test.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    current_app.emit('my respone', json, callback=messageReceived)




if __name__ == '__main__':
    socketio.run(application, port='5001', debug=True)
