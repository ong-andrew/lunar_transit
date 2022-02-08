import ephem

place = ephem.Observer()
place.date = '2022/02/05'
place.lat = '5.042251'
place.lon = '100.665398'
m = ephem.Moon()
print(place.next_transit(m))
print(place.next_rising(m))
