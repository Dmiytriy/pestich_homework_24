from flask import Flask

from views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main_bp)

    return app

# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
# app.register_blueprint(main_bp)


