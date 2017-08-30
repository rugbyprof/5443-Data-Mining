<sup>source: https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/</sup>

### Dot Product

The dot product can be used to find the length of a vector or the angle between two vectors. The cross product is used to find a vector which is perpendicular to the plane spanned by two vectors.

### Algebraic Def
![](https://d3vv6lp55qjaqc.cloudfront.net/items/232Q0V3L3c3C0f29301k/dot_prduct_formula.png)

### Geometric Def
![](https://d3vv6lp55qjaqc.cloudfront.net/items/3S0x092B3x3M0H0l3g2b/dot_product_geometric.png)

Using the dot product to explore more features in Numpy.

```python
a = np.array([1,2])
b = np.array([2,1])
dot = 0

for e,f in zip(a,b):
    dot += e*f
    

# dot = 4

a*b

np.sum(a*b)

(a*b).sum()

np.dot(a,b)

a.dot(b)
b.dot(a)

# calculate angle between a and b
# squaroot of the sum between each element squared

#magnitude way 1
amag = np.sqrt((a*a).sum())

#magnitude linalg way (norm = length or size) 
amag = np.linalg.norm(a)

# calculate the angle
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle) # in radians

### Dot Product Speed Comparison

 
