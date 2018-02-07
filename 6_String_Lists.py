## Ask the user for a string and print out whether this string is a palindrome
## or not. (Palindrom is a string that reads the same forwards and backwards)

print('Enter a string')
word1 = input()
if word1 == word1[::-1]:
    print('It is a palindrome')
else:
    print('Not a palindrome')
