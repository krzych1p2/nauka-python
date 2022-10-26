from cmath import isnan
import numbers
from pickle import FALSE
import sys
import random
no_of_tries = 5
word = "kamila"
user_word = []
used_letters = []
word_list = []
list_letters = []
len_list_letters = 6

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

def words(how_many_word):
    
    list_letters = open('słowa.txt',"r", encoding="utf-8").readlines()
    
    while how_many_word != -1:
        word = random.choice(list_letters).strip()
        if word not in word_list:
            word_list.append(word)
            how_many_word -= 1
    return print(word_list)
       
def how_words(how_many_word):
    while True:
        how_many_word = input("Podaj ile słów chcesz odgadnąć")
        try:
            how_many_word=int(how_many_word)
            if how_many_word > 10 or how_many_word <= 0:
                print("Musisz Podać liczbe! od 1 do " ,len_list_letters)
            else:
                return how_many_word
        except(ValueError,TypeError):
            print("Musisz podac liczbe")
        

how_many_word= 1
print('Witaj w grze Wisielec')
how_words(how_many_word)
words(how_many_word)

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


