import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Movie, Actor

from auth import AuthError, requires_auth

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

@app.route('/')
def welcome():
    """
        Welcome
    """

    return jsonify({
        'success': True,
        'message':"welcome to capstone"
    }), 200

#  Movies
#  ----------------------------------------------------------------

@app.route('/movies')
@requires_auth('get:movies')
def get_movies(payload):
    """
        Gets all Movies
    """

    data = Movie.get_all()

    return jsonify({
        'success': True,
        'all_movies': data
    }), 200


@app.route('/movies/create', methods=['POST'])
@requires_auth('post:movies')
def create_movies(payload):
    """
    Creates a new movie
    """

    request_data = request.get_json()

    title = request_data.get('title')
    description = request_data.get('description')
    category = request_data.get('category')

    movie = Movie(
        title=title,
        description=description,
        category=category
    )

    db.session.add(movie)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'the movie ' + title + ' was successfully listed',
        'movie': movie.format()
    }), 201


@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(id):
    """
        Deletes a movie by ID
    """

    movie = db.session.query(Movie).filter_by(id=id).first()

    if not movie:
        abort(404)
    title = movie.title
    db.session.delete(movie)
    db.session.commit()

    return jsonify({
        "success": True,
        'message': 'Movie ' + title + ' successfully deleted.'
    }), 201


@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(id):
    """
        Updates movie title
    """
    request_data = request.get_json()
    movie = Movie.query.filter_by(id=id).first()

    if not movie:
        abort(404)

    movie.title = request_data.get("title", movie.title)
    db.session.commit()

    return jsonify({
        'success': True,
        'movie': movie.format()
    }), 200


#  Actors
#  ----------------------------------------------------------------

@app.route('/actors')
@requires_auth('get:actors')
def get_actors(payload):
    """
        Gets all actors
    """

    data = Actor.get_all()

    return jsonify({
        'success': True,
        'all_actors': data
    }), 200


@app.route('/actors/create', methods=['POST'])
@requires_auth('post:actors')
def create_actor(payload):
    """
    Creates a new actor
    """

    request_data = request.get_json()

    name = request_data.get('name')
    age = request_data.get('age')
    gender = request_data.get('gender')

    actor = Actor(
        name=name,
        age=age,
        gender=gender
    )

    db.session.add(actor)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Actor was successfully listed',
        'actor': actor.format()
    }), 201


@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(id, payload):
    """
        Deletes a actor by ID
    """

    actor = db.session.query(Actor).filter_by(id=id).first()

    if not actor:
        abort(404)
    name = actor.name
    db.session.delete(actor)
    db.session.commit()

    return jsonify({
        "success": True,
        'message': 'Actor ' + name + ' successfully deleted.'
    }), 201


@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(id, payload):
    """
        Updates an actor
    """
    request_data = request.get_json()
    actor = Actor.query.filter_by(id=id).first()

    if not actor:
        abort(404)

    actor.name = request_data.get("name", actor.name)
    actor.age = request_data.get("age", actor.age)
    actor.gender = request_data.get("gender", actor.gender)
    db.session.commit()

    return jsonify({
        'success': True,
        'actor': actor.format()
    }), 200


# ----------------------------------------------------------------------------#
# Error Handling.
# ----------------------------------------------------------------------------#


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def permission_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.__dict__
    }), 401


# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#


# specify port manually:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
