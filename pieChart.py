import matplotlib.pyplot as plt

#defining labels
activiteis = ['eat', 'sleep', 'work', 'play']

# portion covered by each labels
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

plt.pie(slices, labels = activiteis, colors= colors,
        startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
        radius=1.2, autopct='%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()
