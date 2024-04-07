import art
print(art.logo)
print("\n Welcome to the Secret Auction Program. \n")

auction_list = []
continue_auction = True

def get_auction(name, bid):
    new_auction = {
        "name": name,
        "bid": bid,
    }
    auction_list.append(new_auction)
      
highest_bid = 0
while continue_auction:
    name = input("\n What's your name?: ")
    bid = int(input("\n What's your bid?: $"))
    get_auction(name, bid)
    auction = input("\n Are there any other bidders? 'yes/no'. ")
    if auction.lower() == "no":
        continue_auction = False
        for person in auction_list:
            if person["bid"] > highest_bid:
                highest_bid = person["bid"]
                winner_name = person["name"]
        print(f"\n The winner is {winner_name} with a bid of ${highest_bid}. \n")
        print("Thanks for using our secret auction program, goodbye.\n")
    else:
        continue_auction = True
        
# from art import logo

# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
  