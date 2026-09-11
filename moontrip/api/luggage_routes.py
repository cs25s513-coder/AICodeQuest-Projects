# ============================================================
# TASK M9 — Luggage fees
# Files for this task:
#   logic/luggage.py
#   api/luggage_routes.py       <- this file
#   web/src/tasks/LuggageEstimator.jsx
# TODO(M9):
#   [ ] implement luggage_fee() in logic/luggage.py
#   [ ] implement this route: POST /api/luggage/fee
#       body: {"items": [{"weight_kg": number, "medical": bool}, ...],
#              "cabin": str}
#       response: the dict from luggage_fee()
#   [ ] build the luggage estimator
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/luggage/fee", methods=["POST"])
    def luggage_fee_route():
        return jsonify({"error": "not_implemented", "task": "M9"}), 501
