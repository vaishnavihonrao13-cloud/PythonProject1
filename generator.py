#in python ,a generator is special type of function that produces values one at a time ,instead of creating and storing all values in memory at once
#it uses yield
def numbers():
    yield 1
    yield 2
    yield 3
numbers = numbers()
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))

for i in numbers:
    print(i,end=" ")