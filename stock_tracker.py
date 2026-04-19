# Stock Portfolio Tracker

# Hardcoded stock prices (you can modify/add more)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Take user input
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == 'DONE':
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available in price list.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} - Quantity: {quantity}, Price: ${price}, Value: ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} - Quantity: {quantity}, Value: ${investment}\n")
    
    file.write(f"\nTotal Investment: ${total_investment}")

print("\n✅ Portfolio saved to 'portfolio_summary.txt'")