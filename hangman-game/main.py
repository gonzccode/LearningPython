import json
import random

print('---WELCOME TO HANGMAN GAME---')
print("""
      ===========
    ||          |
    ||          0
    ||         \|/
    ||          |
    ||         / \ 
    ||
   /||\______________
""")
print('Instructions:')
print("""
1. Guess the word or phrase you get.
2. You can enter a letter or number.
3. If you enter more characters, only the first letter or number is entered.
5. If you fail more than 5 times, you will lose the game.
6. To exit the game, type exit or EXIT.
Good luck!!!.
""")

confirm = input("Want to start playing? (yes/no): ")
start = True
list_hangman = [
    """
      ===========
    ||          |
    ||          
    ||          
    ||          
    ||         
    ||
   /||\______________
    """,
    """
      ===========
    ||          |
    ||          0
    ||          
    ||          
    ||         
    ||
   /||\______________
   
    """,
    """
      ===========
    ||          |
    ||          0
    ||          |
    ||          |
    ||         
    ||
   /||\______________
   
    """,
    """
      ===========
    ||          |
    ||          0
    ||         \|
    ||          |
    ||         
    ||
   /||\______________
    """,
    """
      ===========
    ||          |
    ||          0
    ||         \|/
    ||          |
    ||         
    ||
   /||\______________
    """,
    """
      ===========
    ||          |
    ||          0
    ||         \|/
    ||          |
    ||         /  
    ||
   /||\______________
   
    """,
    """
      ===========
    ||          |
    ||          0
    ||         \|/
    ||          |
    ||         / \ 
    ||
   /||\______________
    """
]


###function to load the json file
def load_data(path):
    with open(path) as data:
        words = json.load(data)
        return words.get('data')


###function to choose the word
def choosing_word():
    words = load_data('words.json')
    num = random.randint(0, len(words) - 1)
    word = words[num].strip()
    return word


###function to hide the word
def hiding_word(word):
    list_letter = []
    for w in word:
        if w == ' ':
            list_letter.append(' ')
        else:
            list_letter.append('_')
    string_letter = "".join(list_letter).strip()
    return string_letter.upper()


###function to start the game
def hangman_game():
    ###calling the function choosing_word()
    game_word = choosing_word().upper()
    ###calling the function hiding_word()
    hidden_word = hiding_word(game_word)
    ###attempt counter
    count = 0
    while count < 6:
        print('Guess the word or phrase')
        print(list_hangman[count])
        print(hidden_word)
        list_word = list(hidden_word)
        list_index = []
        letter = input('Enter a letter or number: ')
        print("******************************")

        ###after entering the letter or number, select if it is found in the word
        if len(letter) != 0 and letter != " ":
            letter = letter.upper()
            find_letter = game_word.find(letter[0])
            if find_letter != -1:
                for index, gw in enumerate(game_word):
                    if gw == letter:
                        list_index.append(int(index))

                for i in list_index:
                    list_word[i] = letter

                hidden_word = "".join(list_word).strip()
                if hidden_word == game_word:
                    break
            elif letter == "exit" or letter == "EXIT":
                print("Thanks for playing.")
                break
            elif count < 6:
                count = count + 1
                print("Letter or number no found, you have ", 6 - count, " attempts left")
        else:
            count = count + 1
            print("You have not entered a letter or number, you have ", 5 - count, " attempts left")

    ###asking if the word or phrase was successfully obtained
    if count < 6 and hidden_word == game_word:
        print("The word is: ", game_word)
        print("CONGRATULATIONS YOU WON")
    elif count < 6:
        global confirm
        confirm = input("Do you want to play again? (yes/no): ")
        global start
        start = True
    elif count == 6:
        print(list_hangman[count])
        print("SORRY YOU LOST THE GAME")
        print("******************************")
        confirm = input("Do you want to play again? (yes/no): ")
        start = True


###options to start the game
while start:
    if confirm == "yes" or confirm == "YES" or confirm == "y" or confirm == "Y":
        start = False
        print("******************************")
        hangman_game()
    elif confirm == "no" or confirm == "NO" or confirm == "n" or confirm == "N":
        print("Thanks, come back soon.")
        break
    else:
        print("Option not allowed")
        confirm = input("Want to start playing? (yes/no): ")