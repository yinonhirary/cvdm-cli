#check if we have string
def check_str(input):
    if type(input)==type(str):
        return True
    return False

#check if we have integer
def check_int(input):
    if type(input)==type(int):
        return True
    return False

#check if
def check_password(password,user):
    if len(password)>=6 and len(password)<=8 and len(user)>=6 and len(user)<=8:
        return True
    return False
def check_mail(input):
    if ('@' and '.') in input and input.count('@')==1:
        return True
    return False
def check_phone(input):
    if type(int(input))==type(int):
        if len(input) == 10:
            return True
    return False
def check_full_name(input):
    if " " in input:
        return True
    return False
