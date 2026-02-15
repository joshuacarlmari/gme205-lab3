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
