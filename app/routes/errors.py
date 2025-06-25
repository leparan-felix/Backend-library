from flask import Blueprint, jsonify

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad request"), 400

@errors_bp.app_errorhandler(401)
def unauthorized(e):
    return jsonify(error="Unauthorized"), 401

@errors_bp.app_errorhandler(404)
def not_found(e):
    return jsonify(error="Not found"), 404
