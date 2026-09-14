######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("OUL", 1, "14-09-2026")

allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


def find_flight(flights, flight_number):
    if flight_number is None:
        return None
    cleaned = flight_number.strip().upper()
    for key in flights:
        if key.upper() == cleaned:
            return key
    return None


def passenger_exists(passengers, passenger_name):
    if passenger_name is None:
        return False
    cleaned = passenger_name.strip().lower()
    for name in passengers:
        if name.strip().lower() == cleaned:
            return True
    return False


def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    if passenger_name is None or passenger_name.strip() == "":
        return "EMPTY_NAME"

    flight = flights[key]

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    if passenger_exists(flight["passengers"], passenger_name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(passenger_name.strip().title())
    return "OK"


def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[key]
    cleaned = passenger_name.strip().lower()

    for i in range(len(flight["passengers"])):
        if flight["passengers"][i].strip().lower() == cleaned:
            flight["passengers"].pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    if new_gate is None or new_gate.upper() not in allowed_gates:
        return "INVALID_GATE"

    flights[key]["gate"] = new_gate.upper()
    return "OK"


def flight_status(flight):
    capacity = flight["capacity"]
    count = len(flight["passengers"])
    percentage = count / capacity * 100

    if percentage == 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)
    if key is None:
        return None

    return sorted(flights[key]["passengers"])


def total_passengers(flights):
    total = 0
    for flight in flights.values():
        total = total + len(flight["passengers"])
    return total


def any_full_flight(flights):
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False


def all_flights_have_passengers(flights):
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True
