import matplotlib.pyplot as pyplot

# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]

# plotting the points
pyplot.plot(x, y, color='green',linestyle='dashed', linewidth=3, marker='*',markerfacecolor='blue',markersize=12, label = "line 1")

x1 = [1,2,3]
y1 = [4,1,3]
# plotting the line 2 points
pyplot.plot(x1, y1, label = "line 2")

#setting x and y axis range
pyplot.ylim(0,9)
pyplot.xlim(0,9)
# naming the x axis
pyplot.xlabel('x -axis')

# naming the y axis
pyplot.ylabel('y -axis')

#giving a title to my graph
pyplot.title('Some cool customizations!')

#show a legend on the plot
pyplot.legend()
# function to show the plot
pyplot.show()
