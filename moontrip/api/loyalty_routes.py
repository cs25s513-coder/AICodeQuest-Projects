# ============================================================
# TASK M11 — Moon Miles loyalty
# Files for this task:
#   logic/loyalty.py
#   api/loyalty_routes.py       <- this file
#   web/src/tasks/LoyaltyCard.jsx
# TODO(M11):
#   [ ] implement loyalty_status() in logic/loyalty.py
#   [ ] implement this route: GET /api/users/<id>/loyalty
#       query params: today (optional, "YYYY-MM-DD", default to server date)
#       response: the dict from loyalty_status()
#   [ ] build the loyalty tier card with progress to the next tier
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/users/<user_id>/loyalty", methods=["GET"])
    def loyalty_status_route(user_id):
        return jsonify({"error": "not_implemented", "task": "M11"}), 501
