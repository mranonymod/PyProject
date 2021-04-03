import random,string

LowerCase=string.ascii_lowercase
UpperCase=string.ascii_uppercase
SpecialSym='!@#$%^&*-_'
Numerals=string.digits

def genpwd():
    random_source = UpperCase+LowerCase+SpecialSym+Numerals
    # select 1 lowercase
    password = random.choice(LowerCase)
    # select 1 uppercase
    password += random.choice(UpperCase)
    # select 1 digit
    password += random.choice(Numerals)
    # select 1 special symbol
    password += random.choice(SpecialSym)
    for i in range(3,16):
        password += random.choice(random_source)
    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password