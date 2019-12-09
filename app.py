import sqlite3

from flask import Flask, g, render_template

from db import init_db, fetch_list


DATABASE = 'autocms.sqlite'
app = Flask(__name__)


# This is where most of the procedural code lies
# Add DB connection code
def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def list_posts():
    query = '''
        SELECT
            posts.*,
            users.first_name || ' ' || users.last_name AS author
        FROM
            posts INNER JOIN users ON posts.author_id = users.id
        WHERE
            status = 1
    '''
    posts = fetch_list(get_db(), query)
    return render_template('posts.html', posts=posts)


@app.route('/vehicles')
def list_vehicles():
    return render_template('vehicles.html')


@app.route('/admin/posts')
def post_admin():
    return render_template('posts_admin.html')


# Initialize database
init_db(app)
