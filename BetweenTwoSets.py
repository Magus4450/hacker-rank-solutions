'''
    There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

    1. The elements of the first array are all factors of the integer being considered
    2. The integer being considered is a factor of all elements of the second array

    These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

    Example

    a = [2, 6]
    b = [24, 36]

    There are two numbers between the arrays: 6 and 12.

    6%2=0, 6%6=0, 24%6 and 36%6 for the first value.
    12%2=0, 12%6=0 and 24%12=0, 36%12=0 for the second value. Return 2.
'''

def getTotalX(a, b):
    total = 0
    for i in range(1,max(set(a+b))+1):
        icnt = 0
        for j in a:
            if i%j==0:
                icnt += 1
        for j in b:
            if j%i==0:
                icnt += 1
        if icnt == len(set(a+b)):
            total+=1
        print(f"{i}: {icnt}")
    
    return total

  
            
    return total

if __name__ == "__main__":
    a = [1,]
    b = [100,]
    print(getTotalX(a,b))