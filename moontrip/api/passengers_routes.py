# ============================================================
# TASK M10 — Passenger checks
# Files for this task:
#   logic/passengers.py
#   api/passengers_routes.py    <- this file
#   web/src/tasks/PassengerChecks.jsx
# TODO(M10):
#   [ ] implement validate_passengers() in logic/passengers.py
#   [ ] implement this route: POST /api/passengers/validate
#       body: {"passengers": [...], "travel_date": "YYYY-MM-DD"}
#       response: the dict from validate_passengers()
#   [ ] show per-passenger inline errors on the Book page
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/passengers/validate", methods=["POST"])
    def validate_passengers_route():
        return jsonify({"error": "not_implemented", "task": "M10"}), 501
