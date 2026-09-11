# ============================================================
# TASK M7 — Promo codes
# Files for this task:
#   logic/promos.py             <- this file
#   api/promos_routes.py
#   web/src/tasks/PromoCode.jsx
# TODO(M7):
#   [ ] implement apply_promos() in this file
#   [ ] implement the POST /api/promos/apply route
#   [ ] add the promo code field to the Book page checkout summary
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def apply_promos(price_inr, codes, promos, today):
    """Apply promo `codes` to `price_inr` and return the discounted total.

    price_inr: int, the cart total before discounts
    codes: list of code strings entered by the customer
    promos: list of {"code": str, "type": "percent"|"flat", "value": number,
                      "min_spend_inr": int, "max_discount_inr": int (only
                      for "percent" codes), "expires": "YYYY-MM-DD"}
    today: "YYYY-MM-DD"

    Look up each entered code in `promos` (case-sensitive match on
    "code"). Reject a code, with a reason, if:
    - it doesn't match any known promo -> "unknown_code"
    - today > expires -> "expired"
    - price_inr < min_spend_inr -> "below_minimum_spend"

    Of the accepted codes, at most one "percent" code applies: the one
    giving the largest discount (capped at its max_discount_inr). All
    accepted "flat" codes stack on top of that. The final price never
    goes below 0.

    Returns:
      {
        "final_price_inr": int,
        "applied": [{"code": str, "discount_inr": int}, ...],
        "rejected": [{"code": str, "reason": str}, ...]
      }
    """
    raise NotImplementedError("TODO(M7)")
