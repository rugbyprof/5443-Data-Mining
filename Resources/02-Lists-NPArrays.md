## The Numpy Stack 
### Lists vs Numpy Arrays
```python
# create list
L = [1,2,3]

# create np array
A = np.array([1,2,3])

# access list
for e in L:
     print(e)
# prints: [1, 2, 3]


# add to list
L.append(4)
# L now [1, 2, 3, 4]

# error
A.append(4)

# add to list (2nd way)
L = L + [5]
# L is now [1, 2, 3, 4, 5]


# add to np array (error)
A = A + [4,5]


# List version of adding list to itself (L + L)
L2 = []
for e in L:
    l2.append(e + e)
# results [2, 4, 6, 8, 10]


# Np version of adding list to itself (A + A)
A + A
# results [2, 4, 6, 8, 10]
```

- Lists + sign is overloaded for lists to concatenate with lists
- Np Array + sign is overloaded to do vector addition. If array was 2D it would do matrix addition

```python
# Scalar multiplication
2 * A

# List multiplication
2 * L
# results [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Raise list to a power
L**2
#errors

# Solution for power on list
L2 = []
for e in L:
    L2.append(e*e)
    
# results [1, 4, 9, 16, 25] 

A**2
# results [1, 4, 9, 16, 25] 

np.sqrt(A)
np.log(A)
np.exp(A)

# List would require a for loop to apply these functions

```
