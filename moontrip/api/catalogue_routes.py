# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
from flask import jsonify, request

from api import store
from logic.catalogue import get_destination, list_destinations


def register(app):
    @app.route("/api/destinations", methods=["GET"])
    def list_destinations_route():
        destinations = store.load("destinations")
        sort_by = request.args.get("sort_by")
        return jsonify(list_destinations(destinations, sort_by))

    @app.route("/api/destinations/<destination_id>", methods=["GET"])
    def get_destination_route(destination_id):
        destinations = store.load("destinations")
        destination = get_destination(destinations, destination_id)
        if destination is None:
            return jsonify({"error": "not_found"}), 404
        return jsonify(destination)
