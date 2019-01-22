import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Histogram
random_numbers = np.random.normal(0, 1, 1000)
plt.hist(random_numbers, density=True,
         edgecolor='white', facecolor='blue', alpha=0.5)
plt.title('Histogram - Probability Density for Random Numbers')
plt.xlabel('Value of random numbers')
plt.ylabel('Probability Density')
plt.savefig('histogram.png')
plt.close()

# Pie Chart
labels = ['United College - 3272', 'Chung Chi\nCollege - 3147',
          'New Asia\nCollege - 3400']
sizes = [3272, 3147, 3400]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.05, 0.05, 0.05)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=222)

plt.title('Student Population of 3 Colleges in CUHK')
plt.axis('equal')
plt.savefig("pie.png")
plt.close()

# Bar graph
objects = ('Morningside\nCollege', 'S.H. Ho\nCollege', 'C.W. Chu\n College',
           'United\nCollege', 'Chung Chi\nCollege', 'New Asia\nCollege',
           'Shaw\nCollege', 'Wu Yee\nSun\nCollege', 'Lee Woo\nSing College')
y_pos = np.arange(len(objects))
population = [300, 600, 300, 3272, 3147, 3400, 3441, 1200, 1389]

f, ax = plt.subplots(figsize=(10, 8))
plt.bar(y_pos, population, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('No. of Students')
plt.xlabel('Colleges')
plt.title('Student Population of All CUHK Colleges')
plt.savefig("bar.png")
plt.close()


# Scatterplot
N = 500
x_list = np.linspace(0, 1, 100)
y_list = x_list + np.random.rand(100)
colors = (0, 0, 0)
area = np.pi*3

plt.scatter(x_list, y_list, s=area, c=colors, alpha=0.5)
plt.title('Scatter and Line Plot of X List and Y List')
plt.xlabel('X List')
plt.ylabel('Y List')
x = np.arange(0, 2)
y = x
plt.plot(x, y)
plt.savefig("scatter_line.png")
plt.close()
