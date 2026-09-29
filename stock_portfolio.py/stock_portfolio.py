# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "GOOGL": 150,
    "AMZN": 180
}

# Store user's portfolio
portfolio = {}

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, "=$", price)

print("\nEnter the stock name and quantity.")
print("Type 'done' when you have finished.\n")

# Get stock information from the user
while True:

    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print("Please enter a valid number for quantity.\n")
        continue

    portfolio[stock_name] = quantity

    print(stock_name, "added to your portfolio.\n")


# Calculate total investment
total_investment = 0

print("\n======================================")
print("           PORTFOLIO SUMMARY")
print("======================================")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        stock,
        "- Quantity:", quantity,
        "- Price: $", price,
        "- Investment: $", investment
    )

print("--------------------------------------")
print("Total Investment: $", total_investment)
print("======================================")


# Save portfolio results to a text file
with open("portfolio_result.txt", "w") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            stock
            + " | Quantity: " + str(quantity)
            + " | Price: $" + str(price)
            + " | Investment: $" + str(investment)
            + "\n"
        )

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio result saved to 'portfolio_result.txt'.")
