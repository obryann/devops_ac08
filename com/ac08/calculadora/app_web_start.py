""" Página Flask """
from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def index():
    """ Index do Site """
    return 'Index Page!'

if __name__ == '__main__':
    APP.run()
