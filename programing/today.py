country={"China": "Beijing", "America": "Washington.D.C", "British": "London", "Japen": "Tokyo", "North Korea": "Seoul", "Australia": "Canberra", "Russia": "Mosco", "Italy": "Rome", "Germany": "Berlin", "Canada": "Torrento", "Mongolia": "Ulaanbaatar", "Thailand": "Bangkok"}
print("Country\t\t\tCaptical")
countryList=list(country.keys())
countryList.sort()
pass
for countryName in countryList:
    print("%s: \t%s" % (countryName, country[countryName]))


