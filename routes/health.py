from flask import Blueprint, request, jsonify, abort

bp = Blueprint("health", __name__)
@bp.route("/health", methods=["GET"])
def health():
    return "OK"