# Palindrome Checker

word = input("Enter a world :")
inverse = ""
for c in word :
    inverse = c + inverse

if  word == inverse:
    print(f"The world : {word} is Palindrome")

else :
    print(f"The world : {word} is not palindrome")





