# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
#
# Assembles the Flask app: baseline routes plus every task's stub route,
# pre-registered so no task needs to touch this file.
# ============================================================
from flask import Flask

from api import (
    booking_history_routes,
    catalogue_routes,
    deals_routes,
    itinerary_routes,
    launch_windows_routes,
    loyalty_routes,
    luggage_routes,
    mission_status_routes,
    passengers_routes,
    pricing_routes,
    promos_routes,
    refund_routes,
    seating_routes,
    spacecraft_routes,
    trip_stats_routes,
)

BASELINE_MODULES = [
    catalogue_routes,
    spacecraft_routes,
    deals_routes,
]

TASK_MODULES = [
    pricing_routes,  # M1
    launch_windows_routes,  # M2
    booking_history_routes,  # M3
    refund_routes,  # M4
    seating_routes,  # M5
    mission_status_routes,  # M6
    promos_routes,  # M7
    itinerary_routes,  # M8
    luggage_routes,  # M9
    passengers_routes,  # M10
    loyalty_routes,  # M11
    trip_stats_routes,  # M12
]


def create_app():
    app = Flask(__name__)
    for module in BASELINE_MODULES + TASK_MODULES:
        module.register(app)
    return app
