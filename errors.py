from flask import Blueprint, jsonify

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(404)
def not_found(e):
    return jsonify(error="Not Found"), 404


@errors.app_errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad Request"), 400


@errors.app_errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal Server Error"), 500