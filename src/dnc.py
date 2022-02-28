import numpy as np
import math

def convexhull(bucket):
    arr = np.array([[0, 0]])
    minp = np.array(bucket[0])
    maxp = np.array(bucket[0])

    # mencari titik ekstrim
    for i in range(len(bucket)):
        if minp[0] >= bucket[i][0]:
            if (minp[0] == bucket[i][0]) and (minp[1] < bucket[i][1]):
                minp = bucket[i]
            else:
                minp = bucket[i]
        if maxp[0] <= bucket[i][0]:
            if (maxp[0] == bucket[i][0]) and (maxp[1] < bucket[i][1]):
                maxp = bucket[i]
            else:
                maxp = bucket[i]

    # membagi titik-titik menjadi 2 grup
    s1 = np.array([[0, 0]])
    s2 = np.array([[0, 0]])

    for i in bucket:
        if det(minp[0], minp[1], maxp[0], maxp[1], i[0], i[1]) > 0 and\
                not(minp[0] == i[0] and minp[1] == i[1]) and not(maxp[0] == i[0] and maxp[1] == i[1]):
            s1 = np.append(s1, [i], axis=0)
        if det(maxp[0], maxp[1], minp[0], minp[1], i[0], i[1]) > 0 and\
                not(minp[0] == i[0] and minp[1] == i[1]) and not(maxp[0] == i[0] and maxp[1] == i[1]):
            s2 = np.append(s2, [i], axis=0)
    s1 = np.delete(s1, 0, 0)
    s2 = np.delete(s2, 0, 0)

    # rekurens
    arr = np.append(arr, [minp], axis=0)
    arr = np.delete(arr, 0, 0)
    arr = findpoints(arr, s1, minp[0], minp[1], maxp[0], maxp[1])
    arr = np.append(arr, [maxp], axis=0)
    arr = findpoints(arr, s2, maxp[0], maxp[1], minp[0], minp[1])
    arr = np.append(arr, [minp], axis=0)
    return arr


def det(x1, y1, x2, y2, x3, y3):
    # menentukan posisi titik
    # det = 0 jika berada dalam garis, det > 0 jika di kanan garis, det < 0 jika dikiri garis
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3


def rangepl(x1, y1, x2, y2, x0, y0):
    # menentukan jarak titik (x0,y0) ke garis  (x1,y1)(x2,y2)
    return abs(((x2 - x1)*(y1-y0) - (x1 - x0)*(y2-y1))/(math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))))


def findpoints(arr, bucket, x1, y1, x2, y2):
    s1 = np.array([[0, 0]])
    s2 = np.array([[0, 0]])

    if bucket.size == 0: #basis : jika bucket kosong maka arr tidak berubah
        return arr
    else:
        # mencari titik paling jauh dari garis (x1,y1)(x2,y2)
        C = bucket[0]
        for i in bucket:
            if rangepl(x1, y1, x2, y2, i[0], i[1]) > rangepl(x1, y1, x2, y2, C[0], C[1]):
                C = i

        # membagi titik-titik menjadi 2 grup
        for i in bucket:
            if det(x1, y1, C[0], C[1], i[0], i[1]) > 0 and\
                    not(x1 == i[0] and y1 == i[1]) and not(C[0] == i[0] and C[1] == i[1]):
                s1 = np.append(s1, [i], axis=0)
            if det(C[0], C[1], x2, y2, i[0], i[1]) > 0 and\
                    not(x2 == i[0] and y2 == i[1]) and not(C[0] == i[0] and C[1] == i[1]):
                s2 = np.append(s2, [i], axis=0)
        s1 = np.delete(s1, 0, 0)
        s2 = np.delete(s2, 0, 0)

        # rekurens
        arr = findpoints(arr, s1, x1, y1, C[0], C[1])
        arr = np.append(arr, [C], axis=0)
        arr = findpoints(arr, s2, C[0], C[1], x2, y2)
        return arr
