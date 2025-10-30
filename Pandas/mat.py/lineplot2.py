import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.figure(figsize=(10, 4))


plt.subplot(1, 2, 1)  # (rows, columns, index)
plt.plot(x, y1, color='blue', marker='o')
plt.title("Graph 1")


plt.subplot(1, 2, 2)
plt.plot(x, y2, color='orange', marker='s')
plt.title("Graph 2")

plt.tight_layout()
plt.show()
