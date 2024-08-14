def bidder_client(anct):
    most_bid = 0
    pre_most_bid = 0
    if len(anct) <= 1:
        return 1
    elif len(anct) >= 2:
        for i in range(len(anct)):
            if i == 0:
                most_bid = anct[0]
            if anct[i] > most_bid:
                pre_most_bid = most_bid
                most_bid = anct[i]
            elif anct[i] > pre_most_bid:
               pre_most_bid = anct[i]             
                
        if most_bid != pre_most_bid:
            print(f"winner bid is {most_bid} need to pay {pre_most_bid}")
        else:
            print(f"error : have more than one highest bid")            
    
List1 = []
List1 = [int(item) for item in input("Enter All Bid : ").split(" ")]

FunctionBidder  = bidder_client(List1)

if FunctionBidder == 1:
    print("not enough bidder")

