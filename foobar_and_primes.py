from math import sqrt
result = []
def is_prime(num):
    if num == 1: return False
    for i in range(2,int(sqrt(num)+1)): #basically the i*i<n
        if num % i == 0: return False
    return True
for i in range (1,101):
    if is_prime(i): continue
    elif (i%3==0) and (i % 5==0): result.append("FooBar")
    elif i % 3 == 0: result.append("Foo")
    elif i % 5 == 0: result.append("Bar")
    else:
        result.append(i)
print(result[::-1]) #reversed like the picture from email
