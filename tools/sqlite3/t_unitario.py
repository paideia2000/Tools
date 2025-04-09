import re

test = " My gmail is poencima22@gmail.com"

change_email = re.sub(r'\b[A-Za-z0-9#$%&]+@[A-Za-z0-9]+\.[a-z]{2,}\b', "+++++++",test)

print(change_email)
