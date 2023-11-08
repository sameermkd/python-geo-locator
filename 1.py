from geopy.geocoders import Nominatim

geolocator=Nominatim(user_agent="gooapiExercise")

place=input("Enter city name :")

location = geolocator.geocode(place)

print(location)

#pip install geopy