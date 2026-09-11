# ============================================================
# TASK M3 — Booking history
# Files for this task:
#   logic/booking_history.py
#   api/booking_history_routes.py  <- this file
#   web/src/tasks/BookingHistory.jsx
# TODO(M3):
#   [ ] implement filter_bookings() and sort_bookings() in
#       logic/booking_history.py
#   [ ] implement this route: GET /api/users/<id>/bookings
#       query params: status (optional), from_date (optional),
#       sort_by (optional: "launch_date"|"total_inr"|"destination"),
#       descending (optional: "true"|"false")
#       response: the sorted, filtered list of bookings
#   [ ] build the filterable, sortable table on My trips
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/users/<user_id>/bookings", methods=["GET"])
    def user_bookings_route(user_id):
        return jsonify({"error": "not_implemented", "task": "M3"}), 501
