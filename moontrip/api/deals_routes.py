# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
#
# Plain listing for the Deals page. Applying a code at checkout is task
# M7 (see logic/promos.py, api/promos_routes.py) — this route only
# browses codes and is not part of that task.
# ============================================================
from flask import jsonify

from api import store


def register(app):
    @app.route("/api/promos", methods=["GET"])
    def list_promos_route():
        return jsonify(store.load("promos"))
