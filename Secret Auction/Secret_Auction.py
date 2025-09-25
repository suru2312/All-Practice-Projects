import os

from art import logo

print(logo)

print("=====Welcome to the Secret Auction Program=====")

dict = {}

loop = True
while loop:
    bidder_name = input("Enter your name : ")
    bid_price = float(input("Enter your bidding amount : $"))
    
    dict[bidder_name] = bid_price
    
    should_continue = input("Are there any other bidders? (Yes/No) : ").lower()
    
    if should_continue == "yes":
        os.system("cls")
        print("=====Welcome to the Secret Auction Program=====")
        print(logo)
    else:
        loop = False

winner = ""
top_bid = 0
for i in dict:
    if dict[i] > top_bid:
        top_bid = dict[i]
        winner = i

print(f"The winner of this auction is {winner} with a bid of $", top_bid)