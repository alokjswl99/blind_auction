from art import logo
print(logo)
dic={}

def highest_bidder(dict):
    max_bid={}
    for key in dict:
        if max_bid=={}:
            max_bid[key]=dict[key]
            max_key=key
            max_val=dict[key]
        else:
            if dict[key]>max_val:
                max_bid={}
                max_bid[key]=dict[key]
                max_key=key
                max_val=dict[key]
    print(f"The max bid is {max_bid[max_key]} and the winner is {max_key}")

def add_bidder():
    name=input("What is the bidder's name:")
    bid=int(input("What is the bidder's bid:"))
    dic[name]=bid
    more=input("Are there any more bidders? Say yes or no:")
    if more=="yes":
        add_bidder()
    elif more=="no":
        highest_bidder(dic)
add_bidder()
