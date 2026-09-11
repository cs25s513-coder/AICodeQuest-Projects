# ============================================================
# TASK M8 — Itinerary validator
# Files for this task:
#   logic/itinerary.py          <- this file
#   api/itinerary_routes.py
#   web/src/tasks/ItineraryValidator.jsx
# TODO(M8):
#   [ ] implement validate_itinerary() in this file
#   [ ] implement the POST /api/itinerary/validate route
#   [ ] build the itinerary builder listing validation errors
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def validate_itinerary(activities, trip_start, trip_end):
    """Validate a list of planned trip activities.

    activities: list of {"type": str, "date": "YYYY-MM-DD",
                          "start_hour": number, "end_hour": number}
                (start_hour/end_hour are hours-of-day, 0-24)
    trip_start: "YYYY-MM-DD"
    trip_end: "YYYY-MM-DD"

    Checks, in this order, adding one message per violation found:
    - an activity whose date is before trip_start or after trip_end
      ("activity on {date} is outside the trip dates")
    - two activities on the same date whose [start_hour, end_hour)
      ranges overlap ("{type} overlaps with {type} on {date}")
    - more than 2 activities of type "eva" (moonwalks) on the same date
      ("more than 2 moonwalks on {date}")

    Returns an ordered list of message strings (empty list if the
    itinerary is valid).
    """
    raise NotImplementedError("TODO(M8)")
