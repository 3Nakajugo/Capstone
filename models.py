from flask_sqlalchemy import SQLAlchemy

# initiaze db instance

db = SQLAlchemy()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    category = db.Column(db.String(120))

    def __repr__(self):
        return f'<Movie: { self.title }>'

    def get_by_id(self, id):
        return self.query.filter_by(id=id).first_or_404()

    @classmethod
    def get_all(cls):
        movies = cls.query.all()
        results = [
            {
                'title': movie.title,
                'description': movie.description,
                'category': movie.category,
                'id': movie.id
            }
            for movie in movies
        ]

        return results

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category
        }


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Actor: { self.name }>'

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        actors = cls.query.all()
        results = [
            {
                'name': actor.name,
                'gender': actor.gender,
                'age': actor.age,
                'id': actor.id
            }
            for actor in actors
        ]

        return results

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }
