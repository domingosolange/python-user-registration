
def validate_name(name): 
    if len(name) <=2:
        return False
    return True

def validate_email(email):
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    is_upper = False
    is_dig = False

    for caractere in password:
    
        if caractere.isupper():
            is_upper = True

        if caractere.isdigit():
            is_dig = True

    if is_upper == False:
        return False
    if is_dig == False:
        return False
    return True

def validate_user(name, email, password):

    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")
    
    if validate_email(email) == False:
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")


    if validate_password(password) == False:
         raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, "
                         "contains a capital letter and a number.")
    
    return True


def register_user(name, email, password):
    try: 
        validate_user(name, email, password)

    except ValueError:
        return False
    
    user = {
        "name":name,
        "email": email,
        "password":password
    }

    return user


resultado = register_user(
    "Maria",
    "maria@email.com",
    "Senha123"
)

print(resultado)
