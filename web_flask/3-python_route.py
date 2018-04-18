#!/usr/bin/python3
''' This module contains a script that starts a Flask web application '''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(strict_slashes=False):
    ''' This method returns a simple piece of text '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    ''' This method returns a simple piece of text '''
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text, strict_slashes=False):
    ''' This method returns a simple piece of text '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' This method returns a simple piece of text '''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
