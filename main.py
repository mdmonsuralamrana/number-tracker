import phonenumbers
import folium

from number import number

from phonenumbers import geocoder

sanNumber = phonenumbers.parse(number)

numberLocation = geocoder.description_for_number(sanNumber, "en")
print(numberLocation)

## get service provider

from phonenumbers import carrier

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

from opencage.geocoder import OpenCageGeocode

Key = "bfade40536984f89bce9db69f25106eb"

geocoder = OpenCageGeocode(Key)

query = str(numberLocation)

results = geocoder.geocode(query)

##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=numberLocation).add_to(myMap)

## save map in html file

myMap.save("numberLocator.html")

