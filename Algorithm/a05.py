def palindrome(text):
    if len(text) <= 1:
        return True
    return text[0] == text[-1]
text = input("Enter text: ")
if palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
