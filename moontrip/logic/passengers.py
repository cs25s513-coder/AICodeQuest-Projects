# ============================================================
# TASK M10 — Passenger checks
# Files for this task:
#   logic/passengers.py         <- this file
#   api/passengers_routes.py
#   web/src/tasks/PassengerChecks.jsx
# TODO(M10):
#   [ ] implement validate_passengers() in this file
#   [ ] implement the POST /api/passengers/validate route
#   [ ] show per-passenger inline errors on the Book page
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def validate_passengers(passengers, travel_date):
    """Validate a list of passengers for a booking on `travel_date`.

    passengers: list of {"name": str, "age": int,
                          "medical_clearance": bool,
                          "passport_expiry": "YYYY-MM-DD"}
    travel_date: "YYYY-MM-DD"

    Checks per passenger:
    - name is required (non-empty after trimming)
    - age must be between 3 and 80 inclusive
    - age >= 70 requires medical_clearance to be true
    - passport_expiry must be more than 180 days after travel_date

    Returns a dict keyed by passenger index (as a string, e.g. "0"),
    each value a list of error message strings. Passengers with no
    errors are omitted from the result. Returns {} if everyone passes.
    """
    raise NotImplementedError("TODO(M10)")
