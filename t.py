from math import sqrt
import numpy as np

def pol(G):
    R, C = 32500, 1e-8
    pole = (3-G)/(2*R*C)
    pre_root = 5 - 6*G + G**2 #take square root and divide by 2RC
    post = sqrt(abs(5 - 6*G + G**2))/(2*R*C)
    return pole, pre_root, post

g = np.arange(0,7.25,0.25)
for i in range (len(g)):
    print('G=',g[i])
    print('pole, pre root=', print(pol(g[i])))


R, C = 32500, 1e-8
print('2RC=', 2*R*C) 