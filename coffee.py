#STATEMENT OF REQUIREMENTS
#The system should only accept coin integers of 5, 10, 20, or 50
#The change calculation should be in relation to 75 and however much the total_coin_input is over the value of 75


total_input = (coin_input + coin_input2 )
total_input = 75
while total_input <75:
    coin_input = int(input("What's the value of the coin you've entered: "))
    if coin_input != 5 or 10 or 20 or 50:
        print("Enter a Valid Coin Value!")
    if coin_input == 5:
        print("70p Remaining")
    if coin_input == 10:
        print("65p Remaining!")
    if coin_input == 20:
        print("55p Remaining!")
    if coin_input == 50:
        print("25p Remaining!")
    coin_input2 = int(input("What's the value of the 2nd coin you've entered: "))
    if coin_input2 != 5 or 10 or 20 or 50:
        print("Enter a Valid Coin Value!")
    
