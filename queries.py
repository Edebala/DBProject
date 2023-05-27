def getFlights(db):
    result = db.flights.find({},{})
    for item in result:
        print(item)

def getAirplanes(db):
    result = db.airplanes.find({},{})
    for item in result:
        print(item)
