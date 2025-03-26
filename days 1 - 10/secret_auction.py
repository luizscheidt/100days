end_loop = False

bidders = {}

def find_winning_bid(bidders):
    winner_name = ""
    winner_bid = 0
    for person in bidders:
        if int(bidders[person]) > winner_bid:
            winner_bid = int(bidders[person])
            winner_name = person

    print(f"The winner is {winner_name} with a bid of {winner_bid}")


while end_loop == False:
    name = input("What's your name? ")
    bid = input("What's your bid? ")

    bidders[name] = bid

    continue_bidding = input("Is there any other bidders?(Yes or No) ")

    if continue_bidding == "No":
        end_loop = True
        find_winning_bid(bidders)
    elif continue_bidding == "Yes":
        print("\n" * 8)