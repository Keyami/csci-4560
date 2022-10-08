from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('media', __name__)

@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT title, author, publication, genre, copies, availability, isbn, image'
        ' FROM items'
        ' ORDER BY publication DESC'
        ).fetchall()
    return render_template('media/index.html', books=books)

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
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM items WHERE isbn = id', (isbn,))
    db.commit()
    return redirect(url_for('media.index'))
