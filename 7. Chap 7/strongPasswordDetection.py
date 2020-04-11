import pyperclip, re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9].*[0-9])                 # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
    .{10,}                              # at least 10 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if (not mo):
        print("Not strong, bling blong")
        return False
    else:
        print("Long, Strong, and down to get the crypto on")
        return True


userInputPasswordCheck()