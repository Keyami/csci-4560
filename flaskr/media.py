from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('media', __name__)

# The index() function simply fetches the content listed in table 'items' and passes them to index.html as array 'books'
@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT title, author, publication, genre, copies, availability, isbn, image'
        ' FROM items'
        ' ORDER BY publication DESC'
        ).fetchall()
    return render_template('media/index.html', books=books)

# search() simply takes the passed argument and polls the database for it, then it redirects to index to display the results 
@bp.route('/<id>', methods=('GET', 'POST'))
def search(id):
    db = get_db()
    books = db.execute(
        "SELECT *"
        " FROM items WHERE title LIKE '%" + id + "%'"
        " ORDER BY publication DESC"
        ).fetchall()
    return render_template('media/index.html', books=books)

# search_input passes the value entered into the 'search' form to the search() functions
@bp.route('/search', methods=('GET', 'POST'))
def search_input():
    query = request.form['search']
    return redirect('/'+query+'')

# The create() function takes input from the create.html page forms of the same name and adds them to the database.
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication = request.form['publication']
        genre = request.form['genre']
        copies = request.form['copies']
        availability = request.form['availability']
        isbn = request.form['isbn']
        image = request.form['image']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO items (title, author, publication, genre, copies, availability, isbn, image)'
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (title, author, publication, genre, copies, availability, isbn, image)
            )
            db.commit()
            return redirect(url_for('media.index'))

    return render_template('media/create.html')

# Fetches data of the selected item.
def get_post(id):
    book = get_db().execute(
        'SELECT title, author, publication, genre, copies, availability, isbn, image'
                ' FROM items'
                ' WHERE isbn = ?',
        (id,)
    ).fetchone()

    if book is None:
        abort(404, f"Book id {id} doesn't exist.")

    return book

# view() uses the get_post() function to display an item
@bp.route('/<int:id>/view', methods=('GET', 'POST'))
@login_required
def view(id):
    book = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication = request.form['publication']
        genre = request.form['genre']
        copies = request.form['copies']
        availability = request.form['availability']
        isbn = request.form['isbn']
        image = request.form['image']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'SELECT * FROM items',
                ' WHERE isbn LIKE id',
                (title, author, publication, genre, copies, availability, isbn, image)
            )
            db.commit()
            return redirect(url_for('media.index'))

    return render_template('media/update.html', book=book)

# delete() function selects item in table and removes it, then redirects you from its view page to the homepage.
@bp.route('/<int:id>/delete', methods=('GET', 'POST',))
# This is a callback to the login_required function in flaskr.auth, this means a user without a session id will not be able to see this button.
@login_required
def delete(id):
    isbn = id
    error = None
    
    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'DELETE FROM items WHERE isbn'
        )
        db.commit()
        return redirect(url_for('media.index'))
