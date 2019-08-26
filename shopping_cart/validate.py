"""
Validate EMail id and password

Primary conditions for password validation :
1. Minimum 8 characters.
2. The alphabets must be between [a-z]
3. At least one alphabet should be of Upper Case [A-Z]
4. At least 1 number or digit between [0-9].
5. At least 1 character from [ _ or @ or $ ].
"""

from re import search


def validate_email(email):

    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

    if search(regex, email):
        return True

    else:
        return False


def validate_password(password):
    while True:
        if len(password) < 8:
            return False, "Password length minimum 8 characters"
        elif not search("[a-z]", password):
            return False, "Password should contain at least one alphabets of lower case [a-z]"
        elif not search("[A-Z]", password):
            return False, "Password should contain at least one alphabet of Upper Case [A-Z]"
        elif not search("[0-9]", password):
            return False, "Password should contain at least 1 number or digit between [0-9]"
        elif not search("[_@$#]", password):
            return False, "Password should contain At least 1 character from [ _ or @ or $ or #]"
        else:
            len_password = len(password)

            if len_password >= 8 and len_password < 12:
                return True, "Good password"
            elif len_password >= 12:
                return True, "Strong Password"
