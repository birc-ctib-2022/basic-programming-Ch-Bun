from curses.ascii import islower, isupper
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

#initialisation
is_lower = False
is_upper = False
is_numeric = False
is_special = False
pw_length = 0

# Do all the requirement checks here.
for c in password:
 
    pw_length += 1
    if c.islower():
        is_lower = True
    elif c.isupper():
        is_upper = True
    elif c.isnumeric():
        is_numeric = True
    elif c in '$#@':
        is_special = True
#Check if all requirements are fullfilled   
if is_lower and is_numeric and is_special and is_upper and 6 <= pw_length <= 16:
    is_valid = True

print(is_valid)
