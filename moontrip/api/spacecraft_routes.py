# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
from flask import jsonify

from api import store
from logic.spacecraft import get_craft, list_spacecraft


def register(app):
    @app.route("/api/spacecraft", methods=["GET"])
    def list_spacecraft_route():
        spacecraft = store.load("spacecraft")
        return jsonify(list_spacecraft(spacecraft))

    @app.route("/api/spacecraft/<craft_id>", methods=["GET"])
    def get_spacecraft_route(craft_id):
        spacecraft = store.load("spacecraft")
        craft = get_craft(spacecraft, craft_id)
        if craft is None:
            return jsonify({"error": "not_found"}), 404
        return jsonify(craft)
