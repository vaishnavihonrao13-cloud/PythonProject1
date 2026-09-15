def read_file(filename):
    with open(filename,"r")as f:
        for line in f:
            yield line
for line in read_file("data.txt"):
    print(line)
    
def number():
    for n in range(1, 11):
        yield n

def even_number(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n
def square(number):
    for n in number:
        yield n*n
result=square(even_number(number()))
for x in result:
    print(x)