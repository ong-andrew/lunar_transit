import ephem

place = ephem.Observer()
place.date = '2022/02/05'
place.lat = '5.042251'
place.lon = '100.665398'
m = ephem.Moon()
print(bm.next_transit(m))
print(bm.next_rising(m))
