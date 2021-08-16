from werkzeug.utils import redirect
from books_app.config.mysqlconnection import connectToMySQL
from books_app.models import books

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def make_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_author_info_by_id(cls, data):
        query = "SELECT * from authors WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod
    def insert_data(cls, data):
        query = "INSERT INTO favorites (book_id, author_id, created_at, updated_at) VALUES (%(book_id)s, %(author_id)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_favorite_authors(cls, data):
        query = "SELECT * FROM authors JOIN favorites ON favorites.author_id = authors.id WHERE favorites.book_id = %(id)s"
        return connectToMySQL('books_schema').query_db(query, data)

    # @classmethod
    # def get_authors_favorites(cls, data):
    #     query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE favorites.author_id = %(author_id)s"
    #     results = connectToMySQL('books_schema').query_db(query, data)
    #     favorite = cls(results[0])
    #     print("ppppprint:", favorite)
    #     for result in results:
    #         favorite_data = {
    #             "id": result['books.id'],
    #             "title": result['title'],
    #             "num_of_pages": result['num_of_pages'],
    #             "created_at": result['created_at'],
    #             "updated_at": result['updated_at']
    #         }
    #         favorite.favorite_books.append(books.Book(favorite_data))
    #     return favorite


