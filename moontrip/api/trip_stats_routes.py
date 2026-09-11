# ============================================================
# TASK M12 — Mission control stats
# Files for this task:
#   logic/trip_stats.py
#   api/trip_stats_routes.py    <- this file
#   web/src/tasks/MissionStats.jsx
# TODO(M12):
#   [ ] implement trip_stats() in logic/trip_stats.py
#   [ ] implement this route: GET /api/stats
#       response: the dict from trip_stats()
#   [ ] build the stat tiles plus revenue-by-destination bars
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/stats", methods=["GET"])
    def trip_stats_route():
        return jsonify({"error": "not_implemented", "task": "M12"}), 501
