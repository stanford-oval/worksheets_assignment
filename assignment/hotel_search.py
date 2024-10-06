import random
from uuid import UUID, uuid4


def hotel_search(
    hotel_name: str | None,
    location: str | None,
    cost: str | None,
    min_rating: str | None,
    max_rating: str | None,
):
    if min_rating is None or min_rating == "NA":
        min_rating = 0
    if max_rating is None or max_rating == "NA":
        max_rating = 5
    min_rating = int(min_rating)
    max_rating = int(max_rating)

    min_rating_limit = 0
    max_rating_limit = 5

    if hotel_name is None or hotel_name == "NA":
        hotel_name = random.choices(["ShadySide Inn", "Grand Hotel", "Hilton Hotel"])

    if location is None or location == "NA":
        location = random.choices(["New York", "San Francisco", "Los Angeles"])

    if cost is None or cost == "NA":
        cost = random.choices(["cheap", "moderate", "expensive"])

    if min_rating < min_rating_limit or min_rating > max_rating_limit:
        return {
            "message": "Couldn't find any hotels with the given rating range. Please try again.",
        }

    return {
        "hotel_name": hotel_name,
        "location": location,
        "cost": cost,
        "rating": (
            random.randint(min_rating, max_rating)
            if min_rating != max_rating
            else min_rating
        ),
    }
