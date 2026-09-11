# ============================================================
# TASK M7 — Promo codes
# Files for this task:
#   logic/promos.py
#   api/promos_routes.py        <- this file
#   web/src/tasks/PromoCode.jsx
# TODO(M7):
#   [ ] implement apply_promos() in logic/promos.py
#   [ ] implement this route: POST /api/promos/apply
#       body: {"price_inr": int, "codes": [str, ...]}
#       response: the dict from apply_promos()
#   [ ] add the promo code field to the Book page checkout summary
#   [ ] use an AI assistant; tag its lines honestly in the PR
#
# Note: GET /api/promos (api/deals_routes.py) is a separate baseline
# route that just lists codes for the Deals page — not part of this task.
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/promos/apply", methods=["POST"])
    def apply_promos_route():
        return jsonify({"error": "not_implemented", "task": "M7"}), 501
