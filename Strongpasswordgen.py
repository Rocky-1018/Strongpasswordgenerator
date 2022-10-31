from random import *
from secrets import choice
def passwo(no_of_digits):
    password=""
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    symbols=["!","@","#","$","%","^","&","*"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    sel_alphabets=[choice(alphabets) for i in range(randint(no_of_digits//2,no_of_digits//1.5))]
    symnum=symbols+numbers
    sel_symnum=[choice(symnum)for i in range(randint(no_of_digits-len(sel_alphabets),no_of_digits-len(sel_alphabets)))]
    password=sel_alphabets+sel_symnum
    shuffle(password)
    new_password="".join(password)
    return new_password
    




    

