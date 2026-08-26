def isPrime(no):
    i=2
    prime=True
    while (i<no/2):
        if no%i==0:
            prime=False
            break
        i=i+1
        return prime
n=1234
if isPrime(n):
    print("number is prime")
else:
    print("number is not prime")

def a_function(string):
    "This prints value of string"
    return len(string)
print(a_function("Function"))
print(a_function("Python"))
