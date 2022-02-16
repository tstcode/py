# Basic Operations
import numpy as np
a = np.array([1, 2, 3, 4]) #create an array
print(a + 1)
print(a ** 2)



# All arithmetic operates elementwise
a = np.array([1, 2, 3, 4]) #create an array
b = np.ones(4) + 1
print(a - b)
print(a * b)



# Matrix multiplication
c = np.diag([1, 2, 3, 4])
print(c * c)
print(c.dot(c))



# comparisions
a = np.array([1, 2, 3, 4])
b = np.array([5, 2, 2, 4])
print(a == b)
print(a > b)



# Logical Operations
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print(np.logical_or(a, b))
print(np.logical_and(a, b))


# Transcendental functions
a = np.arange(5)
print(np.sin(a))   
print(np.exp(a))   #evaluates e^x for each element in a given input



# Basic Reductions
# computing sums
x = np.array([1, 2, 3, 4])
print(np.sum(x))


# sum by rows and by columns
x = np.array([[1, 1], [2, 2]])
print(x.sum(axis=0))   #columns first dimension
print(x.sum(axis=1))  #rows (second dimension)



#  Other reductions
x = np.array([1, 3, 2])
print(x.min())
print(x.max())
print(x.argmin())# index of minimum element
print(x.argmax())# index of maximum element



#  Logical Operations
print(np.all([True, True, False]))
print(np.any([True, False, False]))



a = np.zeros((50, 50))
print(np.any(a != 0))
print(np.all(a == a))
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
print(((a <= b) & (b <= c)).all())



# Statistics
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
print(x.mean())
print(np.median(x))
print(np.median(y, axis=-1)) # last axis
print(x.std() )         # full population standard dev.

