import random

# def char_input():

#     Name = input("What is your name?")

#     age = int(int("What is your age?"))

#     yearrn = 2025 

#     bday = yearrn - age

#     hund = bday + 100

#     print(f"Hello {Name}, you will turn 100 in the year {hund}")



# def char_input():
#     # Fixed: Added space after question for better formatting
#     name = input("What is your name?: ")
    
#     # Fixed: Used input() to get user input, then convert to int
#     age = int(input("What is your age?: "))

#     numb = int(input("How many times should we print the final answer out?:"))
    
#     # Fixed: Better variable name (current_year instead of yearrn)
#     current_year = 2025
    
#     # Fixed: Calculate birth year correctly
#     birth_year = current_year - age
    
#     # Fixed: Calculate when they turn 100


#     year_turn_100 = birth_year + 100


#     message = f"Hello {name}, you will turn 100 in the year {year_turn_100}"

#     result =( message + "\n")* numb
    
#     # Fixed: Use f-string dfor proper string formatt ing
#     print(result)



def char_input():
    # Get user inputs
    name = input("What is your name?: ")
    age = int(input("What is your age?: "))
    numb = int(input("How many times should we print the final answer out?: "))
    
    # Calculate when they turn 100
    current_year = 2025
    birth_year = current_year - age
    year_turn_100 = birth_year + 100
    
    # Create the message
    message = f"Hello {name}, you will turn 100 in the year {year_turn_100}"
    
    # Print the message the specified number of times on separate lines
    repeated_message = (message + "\n") * numb
    print(repeated_message)  # end="" prevents extra blank line
    return ''


# Next 

def even_or_odd():
    numbz = int(input("Enter a number!: "))

    if numbz % 2 == 0 and numbz % 4 != 0:
        print(f"{numbz} is a multiple of 4!")
        print(f"{numbz} is a even number!")
    elif numbz % 2 == 0 and numbz % 4 == 0:
        print(f"{numbz} is a multiple of 2, and 4!")
    else:
        print(f"{numbz} is an odd number!" )

    return ""


def num_check():
    num = int(input("Input a number to check if it's divisible: " ))
    check = int(input("Input a number to check divisible: " ))

    if num % check == 0:
        print(f"{num} is divisible by {check} ")
    else:
        print(f"{num} isn't divisible by {check}")

    return ""


def lessthan10():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    newlist = []

    for i in a:
         if i <= 5:
            newlist.append(i)

    return newlist

def newnumber():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    newlist = []

    num = int(input("What number do you want?!: "))
    
    for i in a:
        if i <= num:
            newlist.append(i)
    

    return newlist

def divisors():
    
    newlist = []

    div = int(input("Give me a number that you want divisors for!: "))

    x = range(1, div + 1)

    for i in x:
        if div % i == 0:
            newlist.append(i)
        else:
            None
    return newlist


def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    newlist = []



    for i in a:
        for j in b:
            if i == j:
                newlist.append(i)
    
    return newlist

def list_overlap2():
    a = range(1, random.randint(1 ,75))
    b = range(1, random.randint(1, 150))
    newlist = []

    for i in a:
        for j in b:
            if i == j:
                newlist.append(i)

    return newlist


def string_lists():

    example = input("Input a string to determine if it's a palindome or not!: ")


    if example == example[::-1]:
        print(f"'{example}' is a palindome!")

    else:
        print(f"'{example}' isn't a palindome!")


def list_comprehension():
     a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

     newlist = [ i for i in a if i % 2 != 0]
     newlist2 = [ i for i in a if i % 2 == 0]
     return newlist , newlist2

def rock_paper_scissors():

    player_score = 0

    computer_score = 0  

    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    options = ["rock", "paper", "scissors"]

    print("First to 3 wins!")


    while player_score < 3 and computer_score < 3:
        print(f"\nScore - You: {player_score}, Computer: {computer_score}")

        player = input("Rock, Paper, Scissors | Choose one , or write 'end' if you want to quit!:").lower().strip()

    
        if player in options and player != "end":
                print(f"\nPlayer chose {player}")

                Comp = random.choice(options)
                print(f"\nComputer chose {Comp}")

                if player == Comp:
                    print(f"It's a tie!")

                elif beats[player] == Comp:
                    print(f"You win this round!")
                    player_score += 1

                else:
                    print(f"Computer wins this round!")
                    computer_score += 1


        elif player == "end":
                valid = True
                while valid != False:
                    dec = input(f"Are you sure that you want to end the game? Yes/No: " ).lower().strip()
                    if dec == "yes":
                        return ""
                    elif dec != "no":
                        print(f"You need to answer with yes or no , bro. Wrap it up already.")
                        valid = True

                    else:
                        print(f"That's a relief - game resuming")
                        valid = False


        else:
            print("You need to input only rock, paper, or scissors")
            
        
    if player_score == 3:
        print(f"\nCongradulations, you've won the game!")
    else:
        print(f"\nYOU LOST TO A FUCKING BOT, YOU FUCKING MORON! HA HA HA")

    play_again = input(f"\nWould you like to play again? Yes/No").lower().strip()

    if play_again == "no":
        print(f"Thanks for playing")
        return 
    else:
        print(f"Ready for another round, sucka?")
        rock_paper_scissors()

    
import random

def guess_game():
    guesses = 0
    number = random.randint(1, 9)
    print("I'm thinking of a number between 1 and 9!")
    
    game_over = False
    
    while not game_over:
        guess = input("Guess the computer's number, or write 'exit' to give up: ").lower().strip()
        
        if guess == "exit":
            exit_confirmed = False
            while not exit_confirmed:
                confirm = input("Are you sure that you want to exit? Yes/No: ").lower().strip()
                if confirm == "yes":
                    print("Lol you gave up")
                    return  # Exit the entire function
                elif confirm == "no":
                    print("Quit wasting our time, bro.")
                    exit_confirmed = True  # Go back to guessing
                else:
                    print("That didn't make any sense, yes or no, bro")
                    # Loop continues until valid input
        
        else:
            # Try to convert guess to integer
            try:
                guess_num = int(guess)
                guesses += 1
                
                if guess_num == number:
                    print(f"Congratulations! It took you {guesses} try(s) to guess the number {number}!")
                    
                    # Ask if they want to play again
                    play_again_confirmed = False
                    while not play_again_confirmed:
                        play_again = input("Want to do it again? Yes/No: ").lower().strip()
                        if play_again == "yes":
                            print("Coolio, let's do this again!")
                            guess_game()  # Start new game
                            return
                        elif play_again == "no":
                            print("Alright, thanks for playing!")
                            return
                        else:
                            print("That didn't make any sense, yes or no, bro")
                            # Loop continues until valid input
                    
                elif guess_num > number:
                    print("The number is a tad bit too high!")
                    
                elif guess_num < number:
                    print("The number is too low!")
                    
            except ValueError:
                print("Please enter a valid number or 'exit'")

# Run the game

            
def spin_words(sentence):

    newlist = []

    if isinstance(sentence, str):

        for words in sentence.split():
            if len(words) >= 5:
                newword = words[::-1]
                newlist.append(newword)
            else:
                newlist.append(words)
            


    else:
        print(f"You must only return strings, and no digits")
        return ""

    return " ".join(newlist)

def check_prime():



        

# def narcissistic_numbers(value):
    
#     amount = 0


#     for amount in value:
#         amount += 1
    
    

        

#     return False






if __name__ == '__main__':
   print(spin_words("example sentence"))
   print(spin_words(12345))
   print(spin_words("I like to eat chicken and rice"))
   print(spin_words("1 2 princes here before you"))


