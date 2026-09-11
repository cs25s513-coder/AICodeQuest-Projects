# ============================================================
# TASK M8 — Itinerary validator
# Files for this task:
#   logic/itinerary.py
#   api/itinerary_routes.py     <- this file
#   web/src/tasks/ItineraryValidator.jsx
# TODO(M8):
#   [ ] implement validate_itinerary() in logic/itinerary.py
#   [ ] implement this route: POST /api/itinerary/validate
#       body: {"activities": [...], "trip_start": "YYYY-MM-DD",
#              "trip_end": "YYYY-MM-DD"}
#       response: {"errors": [str, ...]}
#   [ ] build the itinerary builder listing validation errors
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/itinerary/validate", methods=["POST"])
    def validate_itinerary_route():
        return jsonify({"error": "not_implemented", "task": "M8"}), 501
