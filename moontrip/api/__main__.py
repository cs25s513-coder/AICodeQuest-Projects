# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
from api.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5101, debug=True)
