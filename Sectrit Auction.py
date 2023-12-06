def secret_auction():
    bidders = {}
    continue_bidding = 'yes'

    while continue_bidding == 'yes':
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: $"))
        bidders[name] = bid

        continue_bidding = input("Is there any other bidder? Type 'yes' or 'no'.")

    highest_bid = 0
    highest_bidder = ''

    for bidder, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")

if __name__ == "__main__":
    secret_auction()