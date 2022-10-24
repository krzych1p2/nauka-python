import sys
no_of_tries = 5
word = "kamila"
user_word = []
used_letters = []
def find_indexes(word,letter):
    indexes = []
    
    for index, letter_in_word in enumerate(word):
        
        if letter == letter_in_word:
            indexes.append(index)
         
    return indexes
for _ in word:
    user_word.append("_")

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób",no_of_tries)
    print("Użyte litery:", used_letters)
    print()

def letter_add():
    letter = input('Podaj litere  ')
    letter = letter.lower()
    while letter.isalpha() == False or len(letter) != 1:
        print("Musisz Podać literę!")
        letter = input('Podaj literę ')
        letter = letter.lower()
    return letter

def check_letter(letter, used_letters):
    while letter in used_letters:
        print("litera już była")
        letter = letter_add()
    used_letters.append(letter)
    return letter       

while True:
    letter = letter_add()
    check_letter(letter,used_letters)
    

    
    found_indexes = find_indexes(word, letter)
    
    if len(found_indexes) == 0:
        print(f"Brak litery {letter} w słowie! ")
        no_of_tries -=1
        
        if no_of_tries ==0:
            print("Game Ower")
            sys.exit(0)
    else:
        for index in found_indexes:
             user_word[index]= letter

        
        if "".join(user_word) == word:
            print(" Brawo to jest to słowo - ",word)
            sys.exit(0)
    show_state_of_game()


