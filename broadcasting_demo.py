import numpy as np

"""
Broadcasting in Python works like this:
   if you try to sum  [1 2 3 4] + 100, Python will compute [1 2 3 4] + [100 100 100 100].

   Another example:

   [1 2 3; 4 5 6] + [100 200 300], Python will compute [1 2 3; 4 5 6] + [100 200 300; 100 200 300]


Practical example. Suppose A is a matrix of food calories, for example:
         Apples  Beef Eggs  Potatoes
 Carb   
 Protein
 Fat

Compute the percentage of calories for Carb, Protein and Fat for each food, without using a foor-loop.
"""
A = np.array([ [56.0, 0.0, 4.4, 68.0],
               [1.2, 104.0, 52.0, 8.0],
               [1.8, 135.0, 99.0, 0.9]])

print("Input Matrix:\n {}\n".format(A))

cal = A.sum(axis=0)
print("Axis sum: {}".format(cal))

percentage = 100 * A / cal.reshape(1,4) # there is no need to call reshape here, but it can be seen as a good practive in order to be sure about what is the shape of the matrix we are multiplying
print("Percentage portion os each element in the column:\n {}\n".format(percentage))

