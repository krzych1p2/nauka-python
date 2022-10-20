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

def check_letter(letter):
    if letter.isalnum() == True and len(letter) == 1:
        print("")
    else:   
        print("podaj litere")



while True:
    letter = input('Podaj litere  ')
    letter = letter.lower()

    

    while letter.isalpha() == False or len(letter) != 1:
        print("Musisz Podać literę!")
        letter = input('Podaj literę ')
        letter = letter.lower()
    
    for leter in used_letters:
            print("Litera juz była")
    
   
    used_letters.append(letter)
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


