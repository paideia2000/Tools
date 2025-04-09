import re
    
while True:
    new_table = input("\nEnter the new value: ").strip().lower()
    if re.fullmatch(r'[A-Za-z]+',new_table):
        print("CORRECT")
        break
    else:
        print("bad")