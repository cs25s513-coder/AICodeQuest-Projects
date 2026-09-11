# ============================================================
# TASK M2 — Mars launch windows
# Files for this task:
#   logic/launch_windows.py
#   api/launch_windows_routes.py  <- this file
#   web/src/tasks/LaunchWindowBadge.jsx
# TODO(M2):
#   [ ] implement is_window_open() and next_launch_window() in
#       logic/launch_windows.py
#   [ ] implement this route: GET /api/destinations/<id>/next-window
#       response: the dict from next_launch_window(), or
#       {"opens": null, "closes": null, "days_until": null} if there is
#       no upcoming window
#   [ ] show a "next window in N days" badge on destination cards
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================
from flask import jsonify


def register(app):
    @app.route("/api/destinations/<destination_id>/next-window", methods=["GET"])
    def next_window_route(destination_id):
        return jsonify({"error": "not_implemented", "task": "M2"}), 501
