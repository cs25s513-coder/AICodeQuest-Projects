# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
from logic.spacecraft import get_craft, list_spacecraft

SPACECRAFT = [
    {"id": "clipper", "name": "Artemis Clipper", "seat_map": ["..", "X."]},
    {"id": "nova", "name": "Starhopper Nova", "seat_map": ["...", "XXX"]},
]


def test_list_spacecraft_adds_seat_summary():
    result = list_spacecraft(SPACECRAFT)
    clipper = next(c for c in result if c["id"] == "clipper")
    assert clipper["total_seats"] == 4
    assert clipper["free_seats"] == 3


def test_list_spacecraft_all_taken():
    result = list_spacecraft(SPACECRAFT)
    nova = next(c for c in result if c["id"] == "nova")
    assert nova["total_seats"] == 6
    assert nova["free_seats"] == 3


def test_list_spacecraft_does_not_mutate_input():
    list_spacecraft(SPACECRAFT)
    assert "total_seats" not in SPACECRAFT[0]


def test_get_craft_found():
    assert get_craft(SPACECRAFT, "nova")["name"] == "Starhopper Nova"


def test_get_craft_not_found():
    assert get_craft(SPACECRAFT, "missing") is None
