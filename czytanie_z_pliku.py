import sys

while True:
    a = input("podaj zmienna")
    try:
        a=int(a)
        if a > 10 or a <= 0:
            print("zakres to 1 - 10")
        else:
            sys.exit(0)
    except(ValueError,TypeError):
        print("Musisz podac liczbe xd")

   