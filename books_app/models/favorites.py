from werkzeug.utils import redirect
from books_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.book_id = data['book_id']
        self.author_id = data['author_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def make_favorite(cls, data):
        query = "INSERT INTO favorites (book_id, author_id, created_at, updated_at) VALUES (%(book_id)s, %(author_id)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)