# ============================================================
# TASK M5 — Seat allocation
# Files for this task:
#   logic/seating.py
#   api/seating_routes.py       <- this file
#   web/src/tasks/SeatMap.jsx
# TODO(M5):
#   [ ] implement allocate_seats() in logic/seating.py
#   [ ] implement this route: POST /api/craft/<id>/allocate
#       body: {"group_size": int}
#       response: {"seats": [[row, col], ...]} or
#       {"seats": null} if the group cannot fit
#   [ ] show the seat map with the allocated seats highlighted
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/craft/<craft_id>/allocate", methods=["POST"])
    def allocate_route(craft_id):
        return jsonify({"error": "not_implemented", "task": "M5"}), 501
