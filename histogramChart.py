import matplotlib.pyplot as plt
# 直方图

# frequencies
ages = [10,20,30,40,50,60,70,80]

#setting the ranges and no. of intervals
range = (0,100)
bins = 10

#plotting a histogram
plt.hist(ages, bins, range, color = 'purple', histtype = 'bar', rwidth = 0.8)

plt.xlabel('age')
plt.ylabel('No. of people')
#plot title
plt.title('My histogram')

# function to show the plot
plt.show()
