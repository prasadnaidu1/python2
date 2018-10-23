def validNumber(phone_number):
    for i,c in enumerate(phone_number):
        if i in [3,7]:
            if c != '-':
                return False
        elif not c.isalnum():
            return False
    return True
