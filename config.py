import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://tbzyqbrglaztiv:c664a80ebff8425aecd9c96939b4b0fc1dd13fa7a922c095715c520fc5d0b8f9@ec2-174-129-33-84.compute-1.amazonaws.com:5432/deplcd4ff5g2e7'
