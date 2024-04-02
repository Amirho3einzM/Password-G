import random
import string

def generator(long_charecter,number=True,special=True):
    letters=string.ascii_letters
    digits=string.digits
    special_char=string.punctuation
    
    charecter=letters
    
    if number:
        charecter+=digits
    if special:
        charecter+=special_char
        
    pwd=""
    meets_criteria=False
    meets_number=False
    meets_special=False
    
    while not meets_criteria or len(pwd)<long_charecter:
        new_char=random.choice(charecter)
        pwd+=new_char
        
        if new_char in digits:
            meets_number=True
        elif new_char in special_char:
            meets_special=True
            
            
        meets_criteria=True
        if number:
            meets_criteria=meets_number
        if special:
            meets_criteria= meets_criteria and meets_special
            
    return pwd


long_pw=int(input("Please Enter Your long PassWord: "))
Number=input("Do you want PassWord Has Number?[y]es & [n]o: ").lower() == "y"
Special=input("Do you want PassWord Has Special Char?[y]es & [n]o: ").lower() == "y"

pwd=generator(long_pw,Number,Special)
print(f"Your Password: {pwd}")
