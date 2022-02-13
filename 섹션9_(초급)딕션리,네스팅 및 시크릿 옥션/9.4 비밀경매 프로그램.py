# from replit import clear #이거 어찌하는거야 모듈인거 같은데
from turtle import clear
from art import logo
print(logo)

bids = {} # 입찰
bidding_finished = False # 입찰이 끝났는지를 확인하는 변수 선언
# 입찰이 끝나지 않았다면 반복문에 돌아간다
# no일때 반복문에서 빠져나가고 그뒤에 가장 높은 입찰가를 쓴 사람을 딕셔너리에서 찾아
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"나": 123 , "너" : 321}일때 너가 더 금액을 많이 써서 이겼다라는걸 bidding_record에서 알수 있다
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            # highest_bid가 0으로부터 시작해 한번 반복하게 되면 bidder은 나가 되고 나에대한 키 값이 bid_amount가 되서 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price # bids에 {'name': price,}
    should_contiue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_contiue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_contiue == "yes":
        clear()