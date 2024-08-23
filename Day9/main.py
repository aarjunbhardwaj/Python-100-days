from art import logo

def add_bid(bidders, name, amount):
    bidders.append({"name": name, "bid": amount})

def get_highest_bidder(bidders):
    if not bidders:
        return None
    return max(bidders, key=lambda x: x["bid"])

def start_auction():
    print(logo)
    bidders = []
    auction_active = True
    while auction_active:
        name = input("What is your name?: ").title()
        while True:
            try:
                bid = float(input("How much would you like to bid? : $"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        add_bid(bidders, name, bid)
        others = input("Are there other bidders for this auction? Type 'yes' or 'no'.\n")
        if others.lower() == 'no':
            auction_active = False
    highest_bidder = get_highest_bidder(bidders)
    if highest_bidder:
        print(f"The highest bidder is {highest_bidder['name']} with a ${highest_bidder['bid']}")
    else:
        print("No bidders participated in the auction.")
    print("Thank you for your participation.")

start_auction()

