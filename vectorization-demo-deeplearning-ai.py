import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

gain_time = toc-tic

print("c value: {}".format(c))
print("Vectorized version: {} ms".format(1000*(toc-tic)))

c = 0 
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print("c value: {}".format(c))
print("For loop: {} ms".format(1000*(toc-tic)))

gain_time = (toc-tic) / gain_time
print("Vectorization is {} faster than foor loop".format(gain_time))
