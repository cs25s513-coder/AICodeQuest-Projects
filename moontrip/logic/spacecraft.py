# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================


def list_spacecraft(spacecraft):
    """Return `spacecraft` with a computed seat summary for the gallery.

    spacecraft: list of craft dicts (see data/spacecraft.json), each with
    a "seat_map" of row strings ("." = free, "X" = taken).

    Adds "total_seats" and "free_seats" to a copy of each craft dict.
    """
    result = []
    for craft in spacecraft:
        total_seats = sum(len(row) for row in craft["seat_map"])
        free_seats = sum(row.count(".") for row in craft["seat_map"])
        enriched = dict(craft)
        enriched["total_seats"] = total_seats
        enriched["free_seats"] = free_seats
        result.append(enriched)
    return result


def get_craft(spacecraft, craft_id):
    """Return the craft dict with id `craft_id`, or None."""
    for craft in spacecraft:
        if craft["id"] == craft_id:
            return craft
    return None
