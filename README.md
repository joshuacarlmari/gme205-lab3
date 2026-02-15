# Project Title: Spatial Object Systems in Python
## Description: This laboratory extends the custom object model built in Laboratory 2 by integrating:
### 1. Geometry library (Shapely)
### 2. Structured dictionary-based attributes
### 3. Inheritance for shared spatial abstraction

## Reflection
### What changed in the internal representation of Point?
#### In the updated version (Lab 3), it was changed that the coordinates are stored from directly as attributes (lon, lat) to sotring them inside geometry object as geometry. x and geometry.y, respectively. From Lab 2 to Lab 3, the data is structured differently, even though the actual coordinate values remain the same.

### What did not change in the external behavior?
#### There's nothing change in the external behavior. It still produce the same outcone when ran, but the internal implementation is different.

### Where does spatial computation now live?
#### The spatial computation now live in shapely which we installed it to aid us in geometric calculations.

## Reflection C.6
### Why is SpatialObject considered an abstraction, and what real-world idea does it represent in your system?
#### SpatialObject is considered an abstraction because it defines the common properties and behaviors of all spatial entities . In real-world, this represents the things that are spatial such as points, parcels, or buildings which have shared spatial characteristics.

### How does inheritance reduce duplication between classes like Point, Parcel, or Building?
#### Using inheritance reduces duplication by allowing subclasses like Point, Parcel, or Building to share common behavior from SpatialObject. An example is storing geometry or computing bounding boxes without rewriting the same code in each class.

### Why is storing parcel attributes in a dictionary a structural decision rather than a behavioral one?
#### Storing parcel attributes in a dictionary is a structural decision because it organizes the data about the parcel. It describe what the parcel is, not what it does. It holds information rather than functionality.

### If you add a new method (e.g., distance_to()) in SpatialObject, what happens to all subclasses — and why?
#### If you add a new method like distance_to() to SpatialObject, all subclasses automatically inherit that method. This happens because subclasses in Python inherit the behavior of their parent class, so they gain access to any new methods or attributes defined in SpatialObject

### How does this hierarchical design make your spatial system more scalable compared to defining each class independently?

#### This design makes the system more scalable because shared behavior and attributes are defined once in SpatialObject and used by all subclasses. Adding new objects like Parcel or Building is easy since they automatically inherit this functionality.
 


## Reflection
### 1. Why should from_dict() delegate validation to the constructor instead of validating manually inside the method?
#### from_dict() lets the constructor handle validation so rules aren’t repeated. This ensures all objects are checked the same way and keeps from_dict() simple.

### 2. Why is as_dict() implemented inside the object rather than in demo.py or run_lab3.py?
####  as_dict() is implemented inside the object so each object knows how to represent itself. This keeps the code organized, avoids repeating the same conversion in multiple scripts, and makes the object responsible for its own data.

### 3. Why must as_dict() return only primitive data types and not Shapely geometry objects?
#### as_dict() returns only simple data types so it can be easily saved or shared. Shapely objects are too complex to use directly in JSON or dictionaries.

### 4. Why does intersects() belong in the base class instead of being duplicated in Point and Parcel?
#### intersects() belongs in the base class so all spatial objects can use it without repeating code. Repeating it in every class would make the scripts disorganized and repetitive.

### 5. If you add a new spatial subclass tomorrow (e.g., Building), what changes are required for it to support intersects() — and why?
#### There will be no changes in intersects() because it is already in SpatialObjects which is a base class, so all subclasses will have automatically have intersection functionality.


