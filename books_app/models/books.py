from werkzeug.utils import redirect
from books_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_authors = []

    @classmethod
    def make_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW())"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_book_info_by_id(cls, data):
        query = "SELECT * from books WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod
    def get_favorite_books(cls, data):
        query = "SELECT * FROM books JOIN favorites ON favorites.book_id = books.id WHERE favorites.author_id = %(id)s"
        return connectToMySQL('books_schema').query_db(query, data)

