import os

from flask import Flask
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(16)
    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Journal'
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1000 * 1000
    app.config['BOOTSTRAP_BTN_SIZE'] = 'md'
   
    bootstrap.init_app(app)
        
    return app
    
app_ctx = create_app()