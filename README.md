# A map of the Arduino Christmas Contest Winners

In the original winners announcement, Arduino.org used a static map to show winners locations: http://www.arduino.org/blog/1-the-new-blog/announcement-of-christmas-contest-winners

I wasn't very satisfied with it (nor with my location :D), so I wanted to give them a hand and use their data (a list with names and place names) to build a dynamic map using the [geojson-share-maps](https://github.com/bmcbride/geojson-share-maps) utility by Bryan McBride. For georeferencing place names I employed the [OSM Nominatim](http://nominatim.openstreetmap.org/) geocode service via  [GeoPy](https://github.com/geopy/geopy).

The dynamic map can be seen live [here](http://bmcbride.github.io/geojson-share-maps/?src=https://raw.githubusercontent.com/gacarrillor/arduino_winners_map/master/georreferenced.json&fields=name,city&title=Arduino%20Christmas%20Contest%20Winners&title_field=name&attribution=Original%20data:Arduino.org,%20Map%20by%20Germ%C3%A1n%20Carrillo&cluster=true&logo=http://www.arduino.org/images/marchio_arduino.jpg).
