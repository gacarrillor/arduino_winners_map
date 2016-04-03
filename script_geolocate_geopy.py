from geopy.geocoders import Nominatim

geolocator = Nominatim()

lines = []

with open("/docs/tr/otros/map_winners_arduino_org/data.txt") as f:
    for currentLine in f:
        if currentLine is not None: 
            placeName = currentLine.split(" From ")[1].split("(")[0].strip()
            location = geolocator.geocode(placeName)
            try:
                lines.append(",".join([currentLine.split(" From ")[0], placeName, str(location.latitude), str(location.longitude)]))
            except AttributeError:
                print placeName,"had problems..."
    
with open("/docs/tr/otros/map_winners_arduino_org/georreferenced.txt", "wb") as w:
    for line in lines:
        w.write(line)
    
