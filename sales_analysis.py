import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Sales": [50000, 30000, 20000, 60000, 40000]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nProduct Wise Sales:")
print(df.groupby("Product")["Sales"].sum())

df.groupby("Product")["Sales"].sum().plot(kind="bar")

plt.title("Product Wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()
