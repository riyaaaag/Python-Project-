import random

random_number = random.randint(1, 100)
UGuess = None
guesses = 0
score = 0

while(UGuess != random_number):
    print(f"*************************************************")     
    UGuess = int(input("Enter your guesses:"))
    guesses += 1
    print(f'number of guesses left : {10-guesses}')
    if(UGuess == random_number):
       print("You guessed the correct  Number")
    elif(UGuess > random_number):
                print(" The guessed number is high")
    else:
        print("The guessed number is low")
        
        
    if(random_number%2 == 0):
      print('Number you guessed is divisible of 2 and it is even number')   
    elif(random_number%3==0):
        print(' Number you  guessed is divisible of 3 and it is odd number') 
    elif(random_number%5==0):
        print('Number you  guessed is divisible of 5 ') 
    else:
        print("This Number is prime")    
    
    print(f"**************************************************")
    print(f"************BY RIYA GUPTA ************************")     
        
print(f'number guessed by you  in {guesses} guesses')
score = 10-guesses 
print(f'You scored: {score*10}%')
