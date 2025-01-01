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


plt.figure(1)
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
plt.figure(2)
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
plt.figure(3)
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
plt.figure(4)
plt.scatter(month_number,toothpaste, s = 100, label = 'Toothpaste Sales Data')

plt.title('Sales Data (Toothpaste)')
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend(loc="upper left")

plt.grid(color = 'grey', linestyle = '--', linewidth = 1)
plt.xticks(month_number)
plt.yticks([4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000])

plt.show()

"""
Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

The bar chart should look like this.
"""
plt.figure(5)
plt.bar(month_number,facecream, width= -0.25, label = 'Facecream', align='edge')
plt.bar(month_number,facewash, width= 0.25, label = 'Facewash', align='edge')

plt.title('Sales Data (Facecream and Facewash)')
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend(loc="upper left")

plt.grid(color = 'grey', linestyle = '--', linewidth = 1)
plt.xticks(month_number)
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])

plt.show()

"""
Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk

https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib

savefig(fname, *, transparent=None, dpi='figure', format=None,
        metadata=None, bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto', backend=None,
        **kwargs)
"""

plt.figure(6)
plt.bar(month_number,bathingsoap, label = 'Bathing Soap')

plt.title('Sales Data (Bathing Soap)')
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.grid(color = 'grey', linestyle = '--', linewidth = 1)
plt.xticks(month_number)
plt.yticks([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
plt.savefig('Figure_6.png',dpi = 300, transparent = False)
plt.show()


"""
Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
"""

plt.figure(7)
plt.hist(total_profit, label = 'Total Profit')

plt.title('Profit Data')
plt.xlabel("Profit Range (£)")
plt.ylabel("Actual Profit (£)")

plt.legend(loc="upper left")
plt.yticks([0,1,2,3,4,5])

plt.show()
"""
Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart

Note: In Pie chart display Number of units sold per year for each product in percentage.
"""

labels = ["Facecream","Facewash","Toothpaste","Soap","Shampoo","Moisturizer"]
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]

plt.figure(8)
plt.pie(salesData,labels=labels, autopct='%1.1f%%')
plt.axis("equal")
plt.legend(loc='lower right')
plt.title('Sales data')

plt.show()

"""
Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot
"""
plt.figure(9)
plt.subplot(2, 1, 1)
plt.plot(month_number,bathingsoap,label = "Soap",color = 'black',marker = 'o',linewidth = '3')

plt.title('Sales Data (Bath Soap)')
plt.xticks(month_number)
plt.yticks([7000,10000,12500])

plt.subplot(2, 1, 2)
plt.plot(month_number,facewash,label = "Facewash",color = 'red',marker = 'o',linewidth = '3')

plt.title('Sales Data (Facewash)')
plt.xlabel("Month")
plt.ylabel("Sales in Units")

plt.xticks(month_number)
plt.yticks([1500,2000])

plt.show()

"""
Exercise Question 10: Read all product sales data and show it using the stack plot
The Stack plot should look like this.

plt.plot(month_number,facecream, label = "Facecream")
plt.plot(month_number,facewash, label = "Facewash")
plt.plot(month_number,toothpaste, label = "Toothpaste")
plt.plot(month_number,bathingsoap, label = "Soap")
plt.plot(month_number,shampoo, label = "Shampoo")
plt.plot(month_number,moisturizer, label = "Moisturizer")
"""

plt.figure(10)


plt.stackplot(month_number,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,colors=['m','c','r','k','g','y'])

plt.title('Sales Data')
plt.xlabel("Month")
plt.ylabel("Sales Data")

plt.legend(labels = labels, loc = 'upper left')

plt.show()