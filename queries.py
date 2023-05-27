def getFlights(db):
    result = db.flights.find({},{})
    for item in result:
        print(item)
