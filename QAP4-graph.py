#created by: Kyle March-MacCuish
#created on: 2023-11-26
# Program to graph pmts for insurance company
#used the web for the instructions

# Create lists for months and sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = []

# Get sales data for each month
for month in months:
    sales_val = float(input(f"Enter total sales for {month}: $"))
    sales.append(sales_val)

# Plotting the graph
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Total Sales ($) Against Months')
plt.xlabel('Months')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()
