items = ["game","milk","crackers","shorts","gatorade"]
prices = [60, 3, 5, 15, 10]

#1. print "I bought eggs for $3.4"

for item, price in zip(items, prices):
    print(f"I bought {item} for ${price}")

total = 0
for price in prices:
    total += price
print(f"I paid ${total}")

