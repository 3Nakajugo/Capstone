# Capstone

### Introduction

Capstone is a casting agency site that helps in creating movies and managing and assigning actors to those movies.

### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. 
                    "python app.py" to run after installing dependences
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** Your forms
  ├── models.py  *** Your SQL Alchemy models
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ```

Overall:
* Models are located in `models.py`.
* Controllers are located in `app.py`.


### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=app.py
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)

### Endpoints

|Endpoint | Description | Permission | Body   | Response|
| ------  | ------      |------      |------  |------   |
|GET /actors| Fetches actors | None | None | list of drinks |
|GET /movies| Fetches drinks |get:drinks-detial | None | list of drinks |
|POST /actors| Creates new actor |post:actors | `{}` | list of actors |
|POST /movies| Creates new movie |post:movies | `{}` | list of movies |
|PATCH /actors/<int:id>| Updates an actor |patch:actors | `{}` | list of actors |
|PATCH /movies/<int:id>| Updates a movie |patch:movies | `{}` | list of movies |
|DELETE /actors/<int:id>| deletes an actor |delete:actors |None | id of deleted actor |
|DELETE /movies/<int:id>| deletes a movie |delete:movies |None | id of deleted movie |
