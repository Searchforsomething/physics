import numpy as np
import matplotlib.pyplot as plt
import math

e0 = 8.85418781762039 * 10 ** (-12)

#функция поиска значения потенциальной энергии
def findw(x, y):
    angle1 = x * math.pi / 5
    angle2 = y * math.pi / 5
    global e0, p1, p2, r
    w = p1 * p2 * (math.cos(angle1 - angle2) - 3 * math.cos(angle1) * math.cos(angle2))/(4 * math.pi * e0 * r ** 3)
    return w


print('введите значение p1')
p1 = int(input())
print('введите значение p2')
p2 = int(input())
print('введите значение r')
r = int(input())

#моделирование
coord_x = np.empty((11, 11))
coord_y = np.empty((11, 11))
coord_w = np.empty((11, 11))
minw = 1000
minw_coord = []
for i in range(11):
    for j in range(11):
        coord_x[i, j] = i / 5
        coord_y[i, j] = j / 5
        w = findw(i, j)
        coord_w[i, j] = w
        if w < minw:
            minw_coord.clear()
            minw_coord.append([i / 5, j / 5])
            minw = w
        if w == minw and [i / 5, j / 5] not in minw_coord:
            minw_coord.append([i / 5, j / 5])

print("значения, при которых потенциальная энергия минимальна:")
for coord in minw_coord:
    print("первый угол:", int(coord[0]), "pi")
    print("второй угол:", int(coord[1]), "pi\n")

fig = plt.figure()
wf = fig.add_subplot(111, projection='3d')
plt.title("потенциальная энергия W")
wf.plot_wireframe(coord_x, coord_y, coord_w)
plt.show()