import csv
sales = []
product_sales = {}
category_sales = {}
product_quantity = {}
with open("dataset/sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        product = row["Product"]
        category = row["Category"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        # Calculate total sale
        total = quantity * price

        # Store sales in array
        sales.append(total)

        if product in product_sales:
            product_sales[product] += total
        else:
            product_sales[product] = total

        if category in category_sales:
            category_sales[category] += total
        else:
            category_sales[category] = total

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

total_sales = sum(sales)

average_sales = total_sales / len(sales)

highest_sale = max(sales)

lowest_sale = min(sales)

top_product = max(
    product_sales,
    key=product_sales.get
)

top_category = max(
    category_sales,
    key=category_sales.get
)

print("\n" + "=" * 50)
print("       DAY 14 SALES INSIGHT SYSTEM")
print("=" * 50)

print(f"\nTotal Sales       : ₹{total_sales:,.2f}")
print(f"Average Sale      : ₹{average_sales:,.2f}")
print(f"Highest Sale      : ₹{highest_sale:,.2f}")
print(f"Lowest Sale       : ₹{lowest_sale:,.2f}")

print("\n" + "-" * 50)
print("PRODUCT PERFORMANCE")
print("-" * 50)

for product, amount in product_sales.items():

    print(
        f"{product:<20} ₹{amount:,.2f}"
    )

print("\n" + "-" * 50)
print("PRODUCT QUANTITY")
print("-" * 50)

for product, quantity in product_quantity.items():

    print(
        f"{product:<20} {quantity} units"
    )

print("\n" + "-" * 50)
print("CATEGORY PERFORMANCE")
print("-" * 50)

for category, amount in category_sales.items():

    print(
        f"{category:<20} ₹{amount:,.2f}"
    )

print("\n" + "=" * 50)
print("INSIGHTS")
print("=" * 50)

print(f"\n1. {top_product} generated the highest revenue.")
print(f"2. {top_category} is the best-performing category.")
print("3. Sales data was stored using arrays.")
print("4. Hashing was used for product and category aggregation.")
print("5. The system converts raw data into business insights.")

print("\n" + "=" * 50)
print("PROCESSING COMPLETED SUCCESSFULLY")
print("=" * 50)