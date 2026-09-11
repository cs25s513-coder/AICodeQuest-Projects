# ============================================================
# TASK M3 — Booking history
# Files for this task:
#   logic/booking_history.py    <- this file
#   api/booking_history_routes.py
#   web/src/tasks/BookingHistory.jsx
# TODO(M3):
#   [ ] implement filter_bookings() and sort_bookings() in this file
#   [ ] implement the GET /api/users/<id>/bookings route
#   [ ] build the filterable, sortable table on My trips
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def filter_bookings(bookings, user_id, status, from_date):
    """Return the bookings belonging to `user_id` matching the filters.

    bookings: list of booking dicts (see data/bookings.json)
    user_id: string, required
    status: "upcoming" | "completed" | "cancelled" | None (None = any status)
    from_date: "YYYY-MM-DD" | None (None = no lower bound)

    from_date is inclusive: a booking with launch_date == from_date is
    included.
    """
    raise NotImplementedError("TODO(M3)")


def sort_bookings(bookings, key, descending):
    """Return `bookings` sorted by `key`.

    key: "launch_date" | "total_inr" | "destination"
    descending: bool

    "destination" sorts by the booking's destination_id. Ties (equal
    sort key) are broken by ascending booking id.
    """
    raise NotImplementedError("TODO(M3)")
