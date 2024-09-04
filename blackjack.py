import random
print("Welcome to black jack game ! \n")
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
gameCount = 0
play = True
user = []
computer = []

def usercardIndex():
    user_card_index = random.randint(0,len(cards)-1)
    user_res = cards[user_card_index]
    user.append(user_res)
    return user

def computercardIndex():
    comp_card_index = random.randint(0,len(cards)-1)
    comp_res = cards[comp_card_index]
    computer.append(comp_res)
    return computer

usercardIndex()
computercardIndex()
print(f"Your Deck of cards - {user}")
print(f"Computer deck of cards - {computer}")
while play == True:
    user_inp = input("Do you want to pick another card or stand ? \n type 'y' to pick card and 'n' to stand \n" ).lower()
    if(user_inp == 'y'):
        usercardIndex()
        print(f"Your Deck of cards - {user}")
        if(sum(user) < 16):
            play = True
        elif(sum(user) >= 21):
            play = False
            print("\n" * 50)
            print("BUST !!!! YOU LOST !!!")
            break
        
        computercardIndex()   
        print(f"Computer deck of cards - {computer[:-1]}")
        if(sum(computer) < 16):
            play =  True
        elif(sum(computer) >= 21):
            play = False
            print("\n" * 50)
            print("YOU WIN")
            break
    elif(user_inp == 'n'):
        computercardIndex()   
        if(sum(computer) < 16):
            play =  True
        elif(sum(computer) >= 21):
            play = False
            print("\n" * 50)
            print("YOU WIN !!!")
            break
    else:
        print("Please enter a valid input")
        play = True

print("********** Game Over **********")
print(f"Your Deck of cards - {user}")
print(f"Computer deck of cards - {computer}")



