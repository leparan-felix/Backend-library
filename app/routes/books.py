from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.book import Book
from app.extensions import db

books_bp = Blueprint('books', __name__)

# GET /books (already defined above)

@books_bp.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    data = request.get_json()
    user_id = get_jwt_identity()

    if not data or not all(k in data for k in ("title", "author")):
        return jsonify({"error": "Missing required fields: title, author"}), 400

    new_book = Book(
        title=data["title"],
        author=data["author"],
        description=data.get("description", ""),
        read=data.get("read", False),
        user_id=user_id
    )
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
        "description": new_book.description,
        "read": new_book.read
    }), 201


@books_bp.route('/books/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    data = request.get_json()
    user_id = get_jwt_identity()

    book = Book.query.get_or_404(id)

    if book.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.description = data.get("description", book.description)
    book.read = data.get("read", book.read)

    db.session.commit()

    return jsonify({
        "message": "Book updated successfully",
        "book": {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "read": book.read
        }
    }), 200


@books_bp.route('/books/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    user_id = get_jwt_identity()
    book = Book.query.get_or_404(id)

    if book.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200
