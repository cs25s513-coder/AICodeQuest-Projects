# ============================================================
# TASK M1 — Round-trip price calculator
# Files for this task:
#   logic/pricing.py            <- this file
#   api/pricing_routes.py
#   web/src/tasks/PriceCalculator.jsx
# TODO(M1):
#   [ ] implement trip_price() in this file
#   [ ] implement the POST /api/price route
#   [ ] build the PriceCalculator panel on the Book page
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def trip_price(destination, passengers, cabin, travel_date):
    """Return the round-trip price for `passengers` travelling to
    `destination` on `travel_date`.

    destination: {"base_price_inr": int, "season_surcharge_pct": {"1".."12": int}, ...}
    passengers: list of {"age": int}
    cabin: "economy" | "business" | "lunar_suite"
    travel_date: "YYYY-MM-DD"

    Rules:
    - Cabin multipliers: economy 1.0, business 1.8, lunar_suite 3.0.
    - Each passenger's one-way fare is
      base_price_inr * cabin_multiplier, then discounted by age:
      child (age < 12) pays 50%, senior (age >= 65) pays 80%, everyone
      else pays 100%.
    - Round trip = 2 x the one-way fare (after the age discount).
    - The seasonal surcharge is season_surcharge_pct[month_of(travel_date)],
      applied as a percentage on top of the round-trip subtotal, after
      the age discounts.

    Returns a breakdown dict, e.g.:
      {
        "passenger_fares_inr": [12400, 6200],
        "subtotal_inr": 18600,
        "surcharge_inr": 0,
        "total_inr": 18600
      }

    Example: Moon, base_price_inr 6200, 2 adults, economy, a January
    date with a 0% seasonal surcharge for that example ->
    one-way per adult = 6200, round trip per adult = 12400,
    total_inr = 24800.
    """
    raise NotImplementedError("TODO(M1)")
