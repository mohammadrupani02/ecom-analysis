import pandas as pd

# Load the dataset
try:
    data = pd.read_csv("E-commerce Dataset.csv")
except FileNotFoundError:
    print("Error: The dataset file was not found.")
    exit()

# Check for duplicates and missing values
print("Duplicate Rows:", data.duplicated().sum())
print("Missing Values per Column:\n", data.isnull().sum())

# Drop rows with missing values
data = data.dropna()

# 1. Customer Behavior Analysis
# Customer Order Count
customer_orders = data["Customer_Id"].value_counts()
print("Customer Order Count:\n", customer_orders)

# Unique Customers Count
unique_customers = data["Customer_Id"].nunique()
print("Unique Customers:", unique_customers)

# 2. Device Type Distribution
device_distribution = data["Device_Type"].value_counts()
print("Device Type Distribution:\n", device_distribution)

# 3. Most Common Product Categories by Quantity
most_common_products = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("Most Common Product Categories:\n", most_common_products)

# 4. Average Order Value (AOV) by Gender
aov_by_gender = data.groupby("Gender").agg({'Sales': 'sum', 'Customer_Id': 'count'})
aov_by_gender['AOV'] = aov_by_gender['Sales'] / aov_by_gender['Customer_Id']
print("Average Order Value (AOV) by Gender:\n", aov_by_gender)

# 5. Repeat vs. New Customers
customer_type = data["Customer_Id"].map(lambda x: 'Repeat' if customer_orders[x] > 1 else 'New')
data["Customer_Type"] = customer_type

repeat_customers = data[data["Customer_Type"] == "Repeat"]
new_customers = data[data["Customer_Type"] == "New"]

print("Repeat Customers:\n", repeat_customers)
print("New Customers:\n", new_customers)

# 6. Most Frequent Order Days and Hours
most_frequent_days = data["Date"].value_counts()
print("Most Frequent Order Days:\n", most_frequent_days)

most_frequent_hours = data["Hour"].value_counts()
print("Most Frequent Order Hours:\n", most_frequent_hours)

# 7. Product Contribution to Total Revenue
revenue_by_product = data.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("Product Contribution to Total Revenue:\n", revenue_by_product)

# 8. Monthly Revenue Trend
monthly_revenue = data.groupby("Month")["Sales"].sum()
print("Monthly Revenue Trend:\n", monthly_revenue)

# 9. Profit Margin by Product Category
profit_margin = data.groupby("Product_Category").agg({"Sales": "sum", "Profit": "sum"})
profit_margin["Profit Margin %"] = (profit_margin["Profit"] / profit_margin["Sales"]) * 100
print("Profit Margin by Product Category:\n", profit_margin)

# 10. Underperforming Products
underperforming_products = data.groupby("Product")["Sales"].sum().sort_values()
print("Underperforming Products:\n", underperforming_products)
