from flask import app
from books_app import app
from flask import render_template, redirect, request, session, flash
from books_app.models.books import Book
from books_app.models.authors import Author

@app.route("/")
def index():
    books = Book.get_all_books()
    authors = Author.get_all_authors()
    print(books)
    print(authors)
    return render_template("index.html", all_books = books, all_authors = authors)

@app.route("/new_book")
def new_book():
    books = Book.get_all_books()
    return render_template("new_book.html", all_books = books)

@app.route("/books/<int:book_id>")
def view_book(book_id):
    data = {
        "id": book_id
    }
    book = Book.get_book_info_by_id(data)
    favorite_authors = Author.get_favorite_authors(data)
    authors = Author.get_all_authors()
    return render_template("view_book.html", all_authors = authors, book = book, favorite_authors = favorite_authors, book_id = book_id)

@app.route("/make_book", methods=['POST'])
def create_book():
    data = {
        "title": request.form['book_title'],
        "num_of_pages": request.form['book_num_of_pages']
    }
    Book.make_book(data)
    return redirect("/new_book")

@app.route("/books/<int:book_id>/update", methods=['POST'])
def update_favorite_authors(book_id):
    data = {
        "author_id": int(request.form['author_name']),
        "book_id": int(request.form['book_id'])
    }
    Book.insert_data_into(data)
    return redirect(f"/books/{book_id}")

@app.route("/new_author")
def new_author():
    authors = Author.get_all_authors()
    print(authors)
    return render_template("new_author.html", all_authors = authors)

@app.route("/authors/<int:author_id>")
def view_author(author_id):
    data = {
        "id": author_id
    }
    author = Author.get_author_info_by_id(data)
    favorite_books = Book.get_favorite_books(data)
    books = Book.get_all_books()
    return render_template("view_author.html", author = author, all_books = books, favorite_books = favorite_books, author_id = author_id)

@app.route("/make_author", methods=['POST'])
def create_author():
    data = {
        "name": request.form['author_name']
    }
    Author.make_author(data)
    return redirect("/new_author")

@app.route("/authors/<int:author_id>/update", methods=['POST'])
def update_favorite_books(author_id):
    data = {
        "book_id": int(request.form['book_title']),
        "author_id": int(request.form['author_id'])
    }
    Author.insert_data(data)
    return redirect(f"/authors/{author_id}")