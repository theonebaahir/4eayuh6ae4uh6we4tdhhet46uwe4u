def totalcalc (bill ,tip):
    total = bill*(1+0.01*tip )
    total = round(total,2)
    print(f"Please pay ${total}")
    
    
    
    
totalcalc(150,20)


def cube(number):
    return number*number*number


#number is divisble by 3

def bythree(number):
    if number %3 ==0:
        return cube(number)
    else:
     return False
print(bythree(9))
print(bythree(4))





def lion(x):
    '''this is a recursive function to find the factorial of an integer'''
    
    
    
    if x==0 or x==1:
        return 1
    else:
        return x*lion(x-1)
print(lion.__doc__)
print("the lion of 0 :",lion(0))
print("the lion of 1 :",lion(1))
print("the lion of 2 :",lion(4))
print("the lion of 5 :",lion(5))
print("the lion of 10 :",lion(10))
    #recursion
    
    
        