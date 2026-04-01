bidders = []

print("Welcome to the secret auction program.")

more = "y"

while more == "y":
    bidder_name = input("What is your name? ")
    
    bidder_bid = int(input("What is your bid? "))
    
    bidders.append(
        {"bidder_name":bidder_name,
         "bidder_bid": bidder_bid        
        })
    
    more = input("Are there other bidders? (y/n)")
    print("\n"*50)


highest_bidder = None
highest_bid = 0

for bidder in bidders:
    if bidder["bidder_bid"] > highest_bid:
        highest_bid = bidder["bidder_bid"]
        highest_bidder = bidder["bidder_name"]

print(f"Winner: {highest_bidder} with a bid of: {highest_bid}")
print("\n")
print("All bidders: ")
print("_"*50)
sorted_bidders = sorted(bidders, key=lambda x: x["bidder_bid"], reverse=True)

for bidder in sorted_bidders:
    print(f"{bidder["bidder_name"]}: {bidder["bidder_bid"]}")
