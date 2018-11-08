# DOCS: http://flask.pocoo.org/docs/1.0/quickstart/

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# from flask import request
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# url_for('static', filename='style.css')
# # The file has to be stored on the filesystem as static/style.css.

# from flask import render_template
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# from flask import request
#
# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# OR

# from flask import request
#
# with app.request_context(environ):
#     assert request.method == 'POST'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# To access parameters submitted in the URL (?key=value) you can use the args attribute:
#
# searchword = request.args.get('key', '')

# from flask import request
#
# @app.route('/')
# def index():
#     username = request.cookies.get('username')
#     # use cookies.get(key) instead of cookies[key] to not get a
#     # KeyError if the cookie is missing.

# from flask import make_response
#
# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp

# To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:
#
# from flask import abort, redirect, url_for
#
# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

# LOGGING
# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

# To flash a message use the flash() method, to get hold of the messages
# you can use get_flashed_messages() which is also available in the templates. Check out the Message Flashing for a full example.
