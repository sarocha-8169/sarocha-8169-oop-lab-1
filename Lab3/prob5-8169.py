import functools

def isOdd(n) :
    if n % 2 == 1 and n > 0 :
        return True

def compute_sum_positive_odd_numbers():
    numLst = list(map(int,input("Enter number in the list:").strip().split()))
    oddLst = filter(isOdd, numLst)
    print(functools.reduce(lambda a, b: a + b, oddLst))

if __name__ == '__main__':
    compute_sum_positive_odd_numbers()