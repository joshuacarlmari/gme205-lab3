#from spatial import Point

#p = Point("A", 121.0, 14.6)
#print(p.id, p.geometry.x, p.geometry.y)

#q = Point("X", 150, 14)
#print(q.id, q.geometry.x, q.geometry.y)

#print("BBox:", p.bbox())
#print("Tuple:", p.to_tuple())
#print("Tuple:", q.to_tuple())

#distance = p.distance_to(q)
#print("Distance:", distance)

#print("Distance KM:", p.distance_to(q)) #Trial


#p = Point("A", 121.0, 14.6)
#print("BBox:", p.bbox())
#print("Tuple:", p.to_tuple())

from shapely.geometry import Polygon
from spatial import Parcel

geom = Polygon([
    (0,0),
    (10,0),
    (10,5),
    (0,5)
])

# Dictionary for added structure

attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True

}

parcel = Parcel (parcel_id=101, geometry=geom, attributes=attrs)

print("Parcel BBox:", parcel.bbox())
print("Parcel Zone:", parcel.attributes["zone"])