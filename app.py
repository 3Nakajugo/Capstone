import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Movie, Actor

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
