import os

from flask import (
   Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def create_app():
    # Create Flaskr application instance with the default config.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_pyfile('config.py', silent=True)

    # Verify instance folder has been generated.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import the code from db.py, auth.py, and media.py
    from . import db, auth, media
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(media.bp)
    app.add_url_rule('/', endpoint='index')

    return app
