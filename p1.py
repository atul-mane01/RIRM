
import re
def isValid(s):

    reee = '^\+((?:9[679]|8[035789]|6[789]|5[90]|42|3[578]|2[1-689])|9[0-58]|8[1246]|6[0-6]|5[1-8]|4[013-9]|3[0-469]|2[70]|7|1)(?:\W*\d){0,13}\d$'
    Pattern = re.compile(reee)
    return Pattern.match(s)

s=input("Enter your mobile number to validate")
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")
