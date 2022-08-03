vowel = ['A', 'E', 'I', 'O', 'U']
string = input("Enter a string:")

def upperVowel(s):
    return s.upper()

upVowel = map(upperVowel, string)
vowelStr = [v for v in list(upVowel) if v[0] in 'AEIOU']
print(f'Charecters in the string are {list(string)}')
print(f'The entered string is {string} and the result of convert a vowel to uppercase is \n {list(vowelStr)}')