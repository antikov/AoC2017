import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))):
        if(num%i ==0):
            return False
    return True

def prime_numbers(a,b,step):
    answer = 0
    for i in range(a,b,step):
        if is_prime(i):
            answer += 1
            print(i)
    return answer

b = 105700
c = 122700
step = 17
print(1 + (c-b)//step - prime_numbers(b,c,step))
