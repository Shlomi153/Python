travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Hamburg", "Berlin", "Koln"]
    }
]

def addNewCountry(countryVisited, totalVisits, citiesVisited):
    addCountry = {}
    addCountry["country"] = countryVisited
    addCountry["visits"] = totalVisits
    addCountry["cities"] = citiesVisited

    travel_log.append(addCountry)
 

addNewCountry("Russia", 16, ["St Petersburg", "Moscow"])

for i in travel_log:
    print(i)