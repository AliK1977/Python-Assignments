answer = 22

print("Let's start play the guessing game!")

while True :
    
    guess = int(input("What a two-digit number am I thinking of?"))
    
    if guess < answer :
        print("Little higher...")
        
    elif guess > answer :
        print("Little lower...")
        
    else :
        print("Are you a MINDREADER!!")
        break
