from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views.home import home_route

    app.register_blueprint(home_route, url_prefix=("/"))

    return app