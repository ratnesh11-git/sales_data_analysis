import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('sales.csv')

print("Data:\n", data)

# Total sales
total_sales = data['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Average sales
avg_sales = data['Sales'].mean()
print("Average Sales:", avg_sales)

# Plot graph
plt.plot(data['Month'], data['Sales'], marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()