def addFlight(database,flight_id,airline,origin_airport_code,destination_airport_code,departure_time,arrival_time,status):
    data = {
    "flight_id":flight_id,
    "airline":airline,
    "origin_airport_code":origin_airport_code,
    "destination_airport_code":destination_airport_code,
    "departure_time":departure_time,
    "arrival_time":arrival_time,
    "status":status
    }

    result = database.flights.insert_one(data)
    return result
#   flight_id (primary key): Unique identifier for each flight.
#   airline: Name of the airline operating the flight.
#   origin_airport_code: Code representing the airport of departure.
#   destination_airport_code: Code representing the airport of arrival.
#   departure_time: Scheduled departure time of the flight.
#   arrival_time: Scheduled arrival time of the flight.
#   status: Current status of the flight (e.g., on time, delayed, canceled).
