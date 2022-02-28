# visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
import input_data
import dnc

print("Select Data : ")
print("default -> iris")
print("1 -> iris")
print("2 -> wine")
print("3 -> breast_cancer")
select = int(input(">>>"))

data = input_data.data(select)
df = input_data.dataframe(data)

plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']

if select == 1:
    plt.title('iris')
elif select == 2:
    plt.title('wine')
elif select == 3:
    plt.title('breast_cancer')
else:
    plt.title('iris')

plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [0, 1]].values
    hull = dnc.convexhull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    plt.plot(hull[:, 0], hull[:, 1], colors[i])
plt.legend()

print("Save figure to bin folder? y/[n]")
save = input(">>>")
if save == 'y':
    plt.savefig("../bin/figure.png")
    print("Figure saved as \"Figure.png\" in bin folder")

print("Show figure? [y]/n")
show = input(">>>")
if show == 'n':
    exit()
else:
    plt.show()
