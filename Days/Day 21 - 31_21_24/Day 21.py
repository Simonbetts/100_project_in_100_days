# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	31/12/2024

"""
Day 21: Matplotlib
https://pynative.com/python-matplotlib-exercise/
"""

import matplotlib.pyplot as plt
#print(f'Matplotlib Version: {plt.__version__}\n')

import pandas as pd

df = pd.read_csv('sales.csv')
#df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

#print(df.to_string()) 
#print(df.info())

"""	
Exercise 1: Read Total profit of all months and show it using a line plot
Total profit data provided for each month. Generated line plot must include the following properties: –

X label name = Month Number
Y label name = Total profit

"""

month_number = df ['month_number'].tolist()
facecream = df ['facecream'].tolist()
facewash = df ['facewash'].tolist()
toothpaste = df ['toothpaste'].tolist()
bathingsoap = df ['bathingsoap'].tolist()
shampoo = df ['shampoo'].tolist()
moisturizer = df ['moisturizer'].tolist()


total_units = df ['total_units'].tolist()
total_profit = df ['total_profit'].tolist()



plt.plot(month_number, total_profit)
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid()
plt.xticks(month_number)
plt.title('Company Profit per Month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

"""
Exercise 2: Get total profit of all months and show line plot with the following Style properties
Generated line plot must include following Style properties: –

Line Style dotted and Line-color should be red
Show legend at the lower right location.
X label name = Month Number
Y label name = Sold units number
Add a circle marker.
Line marker color as red
Line width should be 3
The line plot graph should look like this.
"""

plt.plot(month_number, total_units, marker = 'o', linestyle = 'dotted', color = 'red',linewidth = '3',mfc = 'black')
plt.xlabel("Month Number")
plt.ylabel("Total Sold Units")
plt.grid()
plt.xticks(month_number)
plt.title('Units Sold')
plt.yticks([17500,20000, 22500, 25000, 27500, 30000, 32500])
plt.legend(['Total Sold Units'],loc="lower right") 
plt.show()


"""
Exercise 3: Read all product sales data and show it  using a multiline plot
Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

The graph should look like this.

"""

plt.plot(month_number,facecream, marker = 'o',linewidth = '3') 
plt.plot(month_number,facewash, marker = 'o',linewidth = '3')
plt.plot(month_number,toothpaste, marker = 'o',linewidth = '3') 
plt.plot(month_number,bathingsoap, marker = 'o',linewidth = '3') 
plt.plot(month_number,shampoo, marker = 'o',linewidth = '3')
plt.plot(month_number,moisturizer, marker = 'o',linewidth = '3')

plt.title('Units Sold')
plt.xlabel("Month Number")
plt.ylabel("Units Sold")

plt.legend(['Facecream','Facewash','Toothpaste','Bathing Soap','Shampoo','Moisturizer'],loc="upper left") 

#plt.grid()
plt.xticks(month_number)
plt.yticks([1000,2000, 4000, 6000, 8000, 10000,12000,15000,18000])

plt.show()


"""
Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
Also, add a grid in the plot. gridline style should “–“.

The scatter plot should look like this.
"""

### E4 ENTRE HERE

"""
Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

The bar chart should look like this.
"""
### E5 ENTRE HERE

"""
Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
"""
### E6 ENTRE HERE
"""
Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
"""
### E7 ENTRE HERE
"""
Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart

Note: In Pie chart display Number of units sold per year for each product in percentage.
"""
### E8 ENTRE HERE

"""
Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot
"""
### E9 ENTRE HERE

"""
Exercise Question 10: Read all product sales data and show it using the stack plot
The Stack plot should look like this.
"""
### E10 ENTRE HERE