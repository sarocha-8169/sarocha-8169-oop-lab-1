vowel = ['A', 'E', 'I', 'O', 'U']
string = (input("Please enter:"))
stringUpper = string.upper()
vowelString = []
charUpper = list(stringUpper) 

for i in range(len(charUpper)):
    for j in range(len(vowel)):
        if charUpper[i] == vowel[j]:
            vowelString.append(vowel[j])

print(f'char are {charUpper}')
print(f'The entered string is Khon Kaen University and the result of convert a vowel to uppercase is \n {vowelString}')
