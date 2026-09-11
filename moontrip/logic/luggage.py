# ============================================================
# TASK M9 — Luggage fees
# Files for this task:
#   logic/luggage.py            <- this file
#   api/luggage_routes.py
#   web/src/tasks/LuggageEstimator.jsx
# TODO(M9):
#   [ ] implement luggage_fee() in this file
#   [ ] implement the POST /api/luggage/fee route
#   [ ] build the luggage estimator
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def luggage_fee(items, cabin):
    """Return the luggage fee for `items` travelling in `cabin`.

    items: list of {"weight_kg": number, "medical": bool}
    cabin: "economy" | "business" | "lunar_suite"

    Items marked "medical": true never count toward weight or fees.

    Free allowance by cabin: economy 5 kg, business 10 kg,
    lunar_suite 20 kg, shared across all non-medical items combined.

    Weight beyond the free allowance is charged: the first 5 kg of
    excess at Rs.900/kg, anything beyond that at Rs.1,500/kg.

    Returns {"total_weight_kg": number, "free_weight_kg": number,
             "excess_weight_kg": number, "fee_inr": int}.
    """
    raise NotImplementedError("TODO(M9)")
