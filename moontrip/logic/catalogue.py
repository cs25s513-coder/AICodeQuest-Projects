# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================


def list_destinations(destinations, sort_by=None):
    """Return `destinations` sorted for the catalogue page.

    destinations: list of destination dicts (see data/destinations.json)
    sort_by: one of "name", "price", "travel_days", or None

    "price" sorts by base_price_inr, "travel_days" by travel_days, both
    ascending. "name" sorts alphabetically. Any other value (including
    None) returns the destinations in their original order.
    """
    if sort_by == "name":
        return sorted(destinations, key=lambda d: d["name"])
    if sort_by == "price":
        return sorted(destinations, key=lambda d: d["base_price_inr"])
    if sort_by == "travel_days":
        return sorted(destinations, key=lambda d: d["travel_days"])
    return list(destinations)


def get_destination(destinations, destination_id):
    """Return the destination dict with id `destination_id`, or None."""
    for destination in destinations:
        if destination["id"] == destination_id:
            return destination
    return None
