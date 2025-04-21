import string
import random


characters = string.ascii_letters + string.digits  #character and digits (A-Z, a-z) , (0-9)
# while True:
shortcode = ''.join(random.choice(characters) for x in range(6))
print(random.choice(characters))