# ============================================================
# TASK M6 — Mission status tracker
# Files for this task:
#   logic/mission_status.py
#   api/mission_status_routes.py  <- this file
#   web/src/tasks/MissionStatus.jsx
# TODO(M6):
#   [ ] implement mission_phase() in logic/mission_status.py
#   [ ] implement this route: GET /api/missions/<id>/status?h=
#       query params: h (hours since launch, number)
#       response: the dict from mission_phase()
#   [ ] build the progress bar with phase labels on Mission control
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/missions/<mission_id>/status", methods=["GET"])
    def mission_status_route(mission_id):
        return jsonify({"error": "not_implemented", "task": "M6"}), 501
