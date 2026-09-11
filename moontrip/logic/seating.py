# ============================================================
# TASK M5 — Seat allocation
# Files for this task:
#   logic/seating.py            <- this file
#   api/seating_routes.py
#   web/src/tasks/SeatMap.jsx
# TODO(M5):
#   [ ] implement allocate_seats() in this file
#   [ ] implement the POST /api/craft/<id>/allocate route
#   [ ] show the seat map with the allocated seats highlighted
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def allocate_seats(seat_map, group_size):
    """Return the seats allocated to a group of `group_size` passengers.

    seat_map: list of row strings, "." = free seat, "X" = taken seat
    group_size: int, number of seats needed

    Prefer a single row containing `group_size` adjacent free seats.
    Among rows that qualify, pick the first row (lowest index); within
    that row, pick the leftmost matching run of seats.

    If no single row has enough adjacent free seats, fall back to
    filling free seats (not necessarily adjacent) using as few rows as
    possible, still preferring earlier rows and leftmost seats within a
    row.

    Return a list of [row_index, seat_index] pairs, one per passenger,
    in the order seats should be assigned. Return None if the group
    cannot fit in the free seats available anywhere on the craft.
    """
    raise NotImplementedError("TODO(M5)")
