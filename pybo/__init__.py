from flask import Flask

# create_app is fixed name on the system. Don't rename it.
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app