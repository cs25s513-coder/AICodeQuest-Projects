# ============================================================
# TASK M4 — Cancellation & tiered refund policy
# Files for this task:
#   logic/refund.py
#   api/refund_routes.py        <- this file
#   web/src/tasks/RefundCalculator.jsx
# TODO(M4):
#   [ ] implement refund_amount() in logic/refund.py
#   [ ] implement this route: POST /api/refunds/quote
#       body: {"booking_id": str, "cancel_date": "YYYY-MM-DD"}
#       response: the dict from refund_amount()
#   [ ] build the refund quote panel on a booking
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/refunds/quote", methods=["POST"])
    def refund_quote_route():
        return jsonify({"error": "not_implemented", "task": "M4"}), 501
