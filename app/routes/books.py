from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.book import Book
from app.extensions import db

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    book = Book(title=data["title"], author=data["author"], user_id=get_jwt_identity())
    db.session.add(book)
    db.session.commit()
    return jsonify(message="Book added"), 201

@books_bp.route('/books', methods=['GET'])
@jwt_required()
def list_books():
    user_id = get_jwt_identity()
    books = Book.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author, "read": b.read} for b in books])

@books_bp.route('/books/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    book = Book.query.get_or_404(id)
    if book.user_id != get_jwt_identity():
        return jsonify(error="Unauthorized"), 403
    data = request.get_json()
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.read = data.get("read", book.read)
    db.session.commit()
    return jsonify(message="Book updated")

@books_bp.route('/books/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book.user_id != get_jwt_identity():
        return jsonify(error="Unauthorized"), 403
    db.session.delete(book)
    db.session.commit()
    return jsonify(message="Book deleted")
