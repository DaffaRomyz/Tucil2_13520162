# visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
import input_iris
import dnc

data = input_iris.data()
df = input_iris.dataframe(data)

plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']
plt.title('Convex Hull')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [0, 1]].values
    hull = dnc.convexhull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    plt.plot(hull[:, 0], hull[:, 1], colors[i])
plt.legend()
plt.show()
