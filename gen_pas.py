from random import choice, randint
import string
LET = string.ascii_letters
letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letters.extend([x for x in LET])

def gen_pas():
    length = randint(8, 16)
    password = ""
    for i in range(length):
        password += choice(letters)
    return password





