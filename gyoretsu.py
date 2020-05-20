import numpy as np
import random

A=np.random.randint(0,10,(3,3))
B=A=np.random.randint(0,10,(3,3))

C=np.dot(A,B)

D=np.dot(C,A)

print (C)
print (D)