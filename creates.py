def addFlight(database,flight_id,airline,origin_airport_code,destination_airport_code,departure_time,arrival_time,status):
    data = {
    "_id":flight_id,
    "airline":airline,
    "origin_airport_code":origin_airport_code,
    "destination_airport_code":destination_airport_code,
    "departure_time":departure_time,
    "arrival_time":arrival_time,
    "status":status
    }

    result = database.flights.insert_one(data)
    return result

def addAirplane(database,airplane_id,airplane_name,airline,capacity,registration_number):
    data = {
    "_id":airplane_id,
    "airplane_name":airplane_name,
    "airline":airline,
    "capacity":capacity,
    "registration_number":registration_number
    }

    result = database.airplanes.insert_one(data)
    return result

#   flight_id (primary key): Unique identifier for each flight.
#   airline: Name of the airline operating the flight.
#   origin_airport_code: Code representing the airport of departure.
#   destination_airport_code: Code representing the airport of arrival.
#   departure_time: Scheduled departure time of the flight.
#   arrival_time: Scheduled arrival time of the flight.
#   status: Current status of the flight (e.g., on time, delayed, canceled).

#   Airplanes Table:
#   airplane_id (primary key): Unique identifier for each airplane.
#   airplane_name: Name or model of the airplane.
#   airline: Name of the airline that owns the airplane.
#   capacity: Maximum number of passengers the airplane can accommodate.
#   registration_number: Unique registration number of the airplane.

#   Airports Table:
#   airport_code (primary key): Unique code representing each airport.
#   airport_name: Name of the airport.
#   location: Location or city where the airport is situated.
#   country: Country where the airport is located.
#   timezone: Timezone of the airport.
