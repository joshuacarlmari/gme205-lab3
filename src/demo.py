from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)


q = Point("X", 150, 14)
print(q.id, q.geometry.x, q.geometry.y)


print("Point P:", p.to_tuple())
print("Point Q:", q.to_tuple())

distance = p.distance_to(q)
print("Distance:", distance)


