# orig = [[[9, 8], [7, 6]], [[5, 4], [3, 2]]] 

# ski = orig

# orig.append('A')				
# orig[1].append('B')
# orig[0] = 'C'		
# orig[1][0].append
# orig[1][1][1] = 'D'			
# orig = [['E'], ['F']]
# orig[1].append('G')


# print(ski)


# ls = ['', 'co', '']
# print("de".join(ls))  # Output: "decode"

# def no_second(fname):

#     try:
#         fp = open(fname, "r")

#         lines = fp.readlines()

#         fp.close()

#         lines.pop(1)

#         newfp = f"no_{fname}"

#         newfpopen = open(newfp, "w")

#         newfpopen.writelines(lines)

#         newfpopen.close()

#         return True



#     except ValueError:
#         return False


# def  between_e(word):
#     first_e = word.index("e")

#     last_e = word.rindex("e")

#     if first_e == last_e:
#         return word

#     mid = word[first_e: last_e].upper()

#     final_word = word[:first_e] + mid + word[last_e:]

#     return final_word




# if __name__ == '__main__':
#     print(between_e('cekkes'))       # Expected output: bees
#     print(between_e('lever'))      # Expected output: leVer
#     print(between_e('estimate'))   # Expected output: eSTIMATe


def rockpaperscissors():
    
 
    while quit != "quit":
        
        quit = input("Type 'quit' to end")
      
        player1 = ""

        player2 = ""

        while player1 not in ["Rock", "Paper", "Scissors"]:
            player1 = input()
            if player1 not in  ["Rock", "Paper", "Scissors"]:
                print(f"{player1} is invalid. You can only use 'Rock', 'Paper', and 'Scissors'")

        while player2 not in ["Rock", "Paper", "Scissors"]:
            player2 = input()
            if player2 not in ["Rock", "Paper", "Scissors"]:
                print(f"{player2} is invalid. You can only use 'Rock', 'Paper', and 'Scissors'")


        skibidi = 0

        while skibidi == 0: 
            if player1 == player2:
                print(f"TIE! Both players are tied!")

            if player1 == "Rock":
                if player2 == "Paper":
                    print(f"Player 2 wins!")
                    skibidi += 1
                elif player2 == "Scissors":
                    print(f"Player 1 wins!")
                    skibidi += 1
            
            if player1 == "Paper":
                if player2 == "Scissors":
                    print(f"Player 2 wins!")
                    skibidi += 1
                elif player2 == "Rock":
                    print(f"Player 1 wins!")
                    skibidi += 1
            
            if player1 == "Rock":
                if player2 == "Paper":
                    print(f"Player 2 wins!")
                    skibidi += 1
                elif player2 == "Scissors":
                    print(f"Player 1 wins!")
                    skibidi += 1


if __name__ == '__main__':
  rockpaperscissors()


        
        

       