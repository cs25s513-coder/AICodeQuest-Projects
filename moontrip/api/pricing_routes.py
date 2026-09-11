# ============================================================
# TASK M1 — Round-trip price calculator
# Files for this task:
#   logic/pricing.py
#   api/pricing_routes.py       <- this file
#   web/src/tasks/PriceCalculator.jsx
# TODO(M1):
#   [ ] implement trip_price() in logic/pricing.py
#   [ ] implement this route: POST /api/price
#       body: {"destination_id": str, "passengers": [{"age": int}],
#              "cabin": str, "travel_date": "YYYY-MM-DD"}
#       response: the breakdown dict from trip_price()
#   [ ] build the PriceCalculator panel on the Book page
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/price", methods=["POST"])
    def price_route():
        return jsonify({"error": "not_implemented", "task": "M1"}), 501
