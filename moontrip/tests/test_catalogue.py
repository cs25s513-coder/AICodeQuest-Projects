# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
from logic.catalogue import get_destination, list_destinations

DESTINATIONS = [
    {"id": "moon", "name": "The Moon", "base_price_inr": 6200, "travel_days": 3},
    {"id": "mars", "name": "Mars", "base_price_inr": 89000, "travel_days": 210},
    {"id": "aurora", "name": "Orbital Hotel Aurora", "base_price_inr": 3100, "travel_days": 1},
]


def test_list_destinations_default_order():
    result = list_destinations(DESTINATIONS, None)
    assert [d["id"] for d in result] == ["moon", "mars", "aurora"]


def test_list_destinations_sort_by_price():
    result = list_destinations(DESTINATIONS, "price")
    assert [d["id"] for d in result] == ["aurora", "moon", "mars"]


def test_list_destinations_sort_by_name():
    result = list_destinations(DESTINATIONS, "name")
    assert [d["id"] for d in result] == ["mars", "aurora", "moon"]


def test_list_destinations_sort_by_travel_days():
    result = list_destinations(DESTINATIONS, "travel_days")
    assert [d["id"] for d in result] == ["aurora", "moon", "mars"]


def test_get_destination_found():
    assert get_destination(DESTINATIONS, "mars")["name"] == "Mars"


def test_get_destination_not_found():
    assert get_destination(DESTINATIONS, "pluto") is None
