from flask import Blueprint, request, jsonify, abort

bp = Blueprint("index", __name__)

@bp.route("/", methods=["GET"])
def health():
    return "hello"