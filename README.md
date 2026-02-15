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
 


