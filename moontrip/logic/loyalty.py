# ============================================================
# TASK M11 — Moon Miles loyalty
# Files for this task:
#   logic/loyalty.py            <- this file
#   api/loyalty_routes.py
#   web/src/tasks/LoyaltyCard.jsx
# TODO(M11):
#   [ ] implement loyalty_status() in this file
#   [ ] implement the GET /api/users/<id>/loyalty route
#   [ ] build the loyalty tier card with progress to the next tier
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def loyalty_status(bookings, user_id, today):
    """Return the Moon Miles balance and tier for `user_id`.

    bookings: list of booking dicts (see data/bookings.json)
    user_id: string
    today: "YYYY-MM-DD"

    Miles are earned only on that user's "completed" bookings with a
    launch_date in the trailing 365 days ending on `today` (inclusive).
    Rs.10 spent (total_inr) = 1 mile. "cancelled" and "upcoming"
    bookings earn nothing.

    Tiers by total miles: Crater (< 5,000), Orbit (5,000 to < 20,000),
    Apollo (>= 20,000).

    Returns {"miles": int, "tier": str, "next_tier": str | None,
             "miles_to_next": int | None} — next_tier/miles_to_next are
    None when already at Apollo.
    """
    raise NotImplementedError("TODO(M11)")
