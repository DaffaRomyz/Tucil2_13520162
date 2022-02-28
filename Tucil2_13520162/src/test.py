import numpy as np
import dnc
import matplotlib.pyplot as plt
import input_iris
import pandas as pd

#a = np.array([[0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,1],[4,2],[4,3],[5,1]])
#b = dnc.convexhull(a)


#print("final : ",b)
#plt.scatter(a[:, 0], a[:, 1])
#plt.plot(b[:, 0], b[:, 1])
#plt.show()

f = open("out.txt", 'w')

a = input_iris.data()
b = input_iris.dataframe(a)
a = str(a)
f.write(a)
print("END")