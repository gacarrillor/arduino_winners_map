import json

outDict = {}
outDict["type"] = "FeatureCollection"
outDict["features"] = []

with open("/docs/tr/otros/map_winners_arduino_org/georreferenced.txt") as f:
    for line in f:
        fields = line.decode("utf-8").split(",")
        name = fields[0] + fields[1]
        placeName = fields[2]
        lon = fields[4].replace("\n","")
        lat = fields[3]
        feature = {}
        feature["type"] = "Feature"
        feature["properties"] = {"name": name, "city":placeName}
        geometry = {"type": "Point", "coordinates":[ float(lon), float(lat) ]}
        feature["geometry"] = geometry
        outDict["features"].append( feature )
    
    
#Save to file
with open("/docs/tr/otros/map_winners_arduino_org/georreferenced.json", "wt") as j:
    j.write(json.dumps(outDict,ensure_ascii=False,sort_keys=True,indent=3).encode('utf-8'))

print "Done!"
