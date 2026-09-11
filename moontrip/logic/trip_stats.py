# ============================================================
# TASK M12 — Mission control stats
# Files for this task:
#   logic/trip_stats.py         <- this file
#   api/trip_stats_routes.py
#   web/src/tasks/MissionStats.jsx
# TODO(M12):
#   [ ] implement trip_stats() in this file
#   [ ] implement the GET /api/stats route
#   [ ] build the stat tiles plus revenue-by-destination bars
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def trip_stats(bookings, destinations):
    """Return aggregate booking statistics for Mission control.

    bookings: list of booking dicts (see data/bookings.json)
    destinations: list of destination dicts (see data/destinations.json)

    Compute:
    - revenue_by_destination: total_inr summed per destination_id,
      counting only non-cancelled bookings (any status other than
      "cancelled")
    - bookings_by_status: count of bookings per status value
    - average_group_size: mean passenger_count across all bookings
      (2 decimal places)
    - most_popular_destination: the destination_id appearing in the most
      non-cancelled bookings; ties broken alphabetically by
      destination_id

    Returns {"revenue_by_destination": {...}, "bookings_by_status": {...},
             "average_group_size": number, "most_popular_destination": str}.
    """
    raise NotImplementedError("TODO(M12)")
