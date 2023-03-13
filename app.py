import os

from flask import Flask
from src.router.blueprint import Blueprint
from dotenv import load_dotenv


class App:
    def __init__(self):
        self.app = Flask(__name__, template_folder='src/templates', static_folder='public')
        self.blueprint = Blueprint()

    def run(self):
        load_dotenv()
        self.app.secret_key = os.getenv('APP_SECRET_KEY')
        self.app.register_blueprint(self.blueprint.routes(), url_prefix='/')
        self.app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    app = App()
    app.run()
