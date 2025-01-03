import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 4, 6, 8, 17, 12, 14, 16, 21]
plt.pie(x,y,x)
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Simple Graph")
plt.savefig("line.jpg", format="jpg")
plt.show()
plt.close()
