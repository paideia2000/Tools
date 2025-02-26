def valid_name(prompt: str)-> str:
    import re
    while True:
        name: str = input(prompt)
        if name and not re.search(r'["!$%&/()=?¡¨*|123456789]', name):
            return name
        else:
            print("\nERROR Check the field and try again.")

def valid_age(prompt: str)-> int:
    while True:
        try:
            age: int = int(input(prompt))
            if age:
                return age
            else:
                print("\nERROR Check the field and try again.")
        
        except ValueError:
            print("\nERROR The content doesn't must empty and your age must be an integer value.\n")

def valid_username(prompt: str)-> str:
    while True:
        username = input(prompt)
        if username:
            return username
        else:
            print("\nERROR Check the field and try again.")

def valid_email(prompt: str)-> str:
    while True:
        email = input(prompt)
        if email and "@" in email and email.endswith(".com"):
            return email
        else:
            print("\nERROR Check the field and try again.")