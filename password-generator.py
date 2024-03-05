import random
import string

MAX_LEN = random.randint(10, 14)

digits = string.digits
smallLetter = string.ascii_lowercase
upperLetter = string.ascii_uppercase
specialChar = string.punctuation

combineChar = digits + smallLetter + upperLetter + specialChar

randDigit = random.choice(digits)
randSmallChar = random.choice(smallLetter)
randUpperChar = random.choice(upperLetter)
randSpecialChar = random.choice(specialChar)

temp_pass = randDigit + randSmallChar + randUpperChar + randSpecialChar

for i in range(MAX_LEN - 4):
	temp_pass += random.choice(combineChar)

temp_pass = list(temp_pass)
random.shuffle(temp_pass)
password = ''.join(temp_pass)

print(password)