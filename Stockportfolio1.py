class Stock:
    def __init__(self, name, symbol, price, shares):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.shares = shares
    
    def get_value(self):
        return self.price * self.shares
    
    def buy(self, shares):
        self.shares += shares
    
    def sell(self, shares):
        if shares > self.shares:
            print("Error: Not enough shares to sell")
        else:
            self.shares -= shares

# Create some stock objects
apple = Stock("Apple Inc.", "AAPL", 148.48, 500)
google = Stock("Alphabet Inc.", "GOOGL", 2685.08, 100)
amazon = Stock("Amazon.com, Inc.", "AMZN", 3312.53, 50)

# Display the current portfolio
print("Current Portfolio:")
print(apple.name + " (" + apple.symbol + "): $" + str(apple.get_value()))
print(google.name + " (" + google.symbol + "): $" + str(google.get_value()))
print(amazon.name + " (" + amazon.symbol + "): $" + str(amazon.get_value()))

# Buy some shares of Apple and sell some shares of Amazon
apple.buy(100)
amazon.sell(25)

# Display the updated portfolio
print("\nUpdated Portfolio:")
print(apple.name + " (" + apple.symbol + "): $" + str(apple.get_value()))
print(google.name + " (" + google.symbol + "): $" + str(google.get_value()))
print(amazon.name + " (" + amazon.symbol + "): $" + str(amazon.get_value()))
