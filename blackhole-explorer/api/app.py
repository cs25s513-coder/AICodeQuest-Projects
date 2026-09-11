# Minimal placeholder API — deliberately scoped down. See
# blackhole-explorer/README.md and TODO.md for where this is headed.
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/api/status")
    def status():
        return jsonify(
            {
                "message": "BlackHole Explorer API is a placeholder for now.",
                "direction": "Real endpoints (event horizon, time dilation, "
                "tidal forces, ...) come later — see structure.md Part B2.",
            }
        )

    return app
