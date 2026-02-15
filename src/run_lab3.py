from spatial import Point
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



row = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}
p = Point.from_dict(row)
print("FROM DICTIONARY")
print("Point ID:", p.id)
print("Coordinates:", (p.geometry.x, p.geometry.y))
print("Name:", p.name)
print("Tag:", p.tag)


point = Point.from_dict(row)

print(point.as_dict())
print(parcel.as_dict())


inside = Point(id="A", lon=5, lat=2)
outside = Point(id="B", lon=12, lat=6)


print("Point A intersects parcel:", inside.intersects(parcel)) 
print("Point B intersects parcel:", outside.intersects(parcel))