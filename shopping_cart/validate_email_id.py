"""
Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
"""

import re


def validate_password(password):
    while True:
        if len(password) < 8:
            return False, "Password length minimum 8 characters"
        elif not re.search("[a-z]", password):
            return False, "Password length minimum 8 characters"
        elif not re.search("[A-Z]", password):
            return False, "Password should at least one alphabet should be of Upper Case [A-Z]"
        elif not re.search("[0-9]", password):
            return False, "Password length minimum 8 characters"
        elif not re.search("[_@$]", password):
            return False, "Password length minimum 8 characters"
        else:
            return True

    if flag == -1:
        print("Not a Valid Password")
