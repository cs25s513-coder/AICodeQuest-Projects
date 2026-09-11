# ============================================================
# TASK M4 — Cancellation & tiered refund policy
# Files for this task:
#   logic/refund.py             <- this file
#   api/refund_routes.py
#   web/src/tasks/RefundCalculator.jsx
# TODO(M4):
#   [ ] implement refund_amount() in this file
#   [ ] implement the POST /api/refunds/quote route
#   [ ] build the RefundCalculator panel
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def refund_amount(booking, cancel_date):
    """Return the refund for cancelling `booking` on `cancel_date`.

    booking: {"total_inr": int, "launch_date": "YYYY-MM-DD", ...}
    cancel_date: "YYYY-MM-DD"

    Rules, by whole days between cancel_date and launch_date:
    - more than 30 days before launch -> 90% of total_inr
    - 8 to 30 days before launch -> 50% of total_inr
    - 1 to 7 days before launch -> 10% of total_inr
    - launch day or later -> 0

    The cancellation fee is the larger of Rs.500 and 2% of total_inr, but
    the fee never exceeds the refund computed above (so refund never goes
    negative). The final refund_inr is the tiered amount minus the fee.

    Returns {"refund_inr": int, "fee_inr": int, "tier": str}, where tier
    is one of "flexible" (>30 days), "standard" (8-30 days),
    "late" (1-7 days), or "none" (launch day or later).
    """
    raise NotImplementedError("TODO(M4)")
