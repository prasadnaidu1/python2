#raise exception

def validateAge(age):
    if age>0:
        return age
    else:
        raise ValueError("invalid input")