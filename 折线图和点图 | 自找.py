import matplotlib.pyplot as plt

## 画折线图

input_squres = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]
plt.plot(input_squres,squares, linewidth=5)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()


## 画点图
plt.scatter(2, 4, s=200)
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

# 画折线图
import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds,
            edgecolors='none', s=1)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
