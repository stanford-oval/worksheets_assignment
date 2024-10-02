import random
from uuid import UUID, uuid4


def check_ride_availability(
    customer_name,
    departure_location,
    arrival_location,
    service_provider,
    driver_name,
    car_model,
):
    if random.random() > 0.5:
        return {
            "status": "success",
            "booking_available": True,
        }
    else:
        return {
            "status": "success",
            "booking_available": False,
        }


def book_ride(
    customer_name,
    departure_location,
    arrival_location,
    service_provider,
    driver_name,
    car_model,
):
    return {
        "status": "success",
        "booking_id": str(uuid4()),
    }
