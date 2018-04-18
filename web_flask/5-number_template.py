#!/usr/bin/python3
''' This module contains a script that starts a Flask web application '''


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' This method returns a simple piece of text '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' This method returns a simple piece of text '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' This method returns a simple piece of text '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' This method returns a simple piece of text '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_a_number(n):
    ''' This method determines if n is a number '''
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' This method returns HTML if n is an integer '''
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
