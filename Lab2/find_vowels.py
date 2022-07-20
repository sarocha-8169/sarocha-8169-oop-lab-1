import string


def hello_vowels(string, vowels):
    hello = [each for each in string if each in vowels]
    print("Vowel in %s are %s"%(string,hello))

string = input("Enter string input:")    
vowels = "Aa,Ee,Ii,Oo,Uu"

if __name__ == '__main__':
    hello_vowels(string, vowels)