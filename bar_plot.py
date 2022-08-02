import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ("Tom", "Dick", "Harry", "Slim", "Jim")
y_pos = np.arange(len(people))
perfomance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, perfomance, xerr=error, align="center", color="red", ecolor="black")
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis() 	# labels read top-to-bottom
ax.set_xlabel("Perfomance")
ax.set_title("How fast do you want to go today")
plt.show()