# Dictionaries, Nesting and the Secret Auction
# Concepts Practised
# The Python Dictionary
# Nesting Lists and Dictionaries
print("Welcome to the private auction .")
bids = {}
auction_finished = False
while not auction_finished:
    nom = str(input("What is your name? "))
    bid = int(input("What is your bid? $"))
    bids[nom] = bid
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == "yes":
        continue

    else:
        auction_finished = True
winner = ""
winning_bid = 0
for bidder in bids:
    if bids[bidder] > winning_bid:
        winner = bidder
        winning_bid = bids[bidder]
print(f"The winner is {winner} with a bid of ${winning_bid}.")
