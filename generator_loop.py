#numbers=(x for x in range(1,100))
#for x in numbers:
#    print(x)

#square=(x**2 for x in range(1,6))
#for x in square:
 #   print(x,end="  ")

#def even_numbers(limit):
   # for n in range(1,limit+1):
  #      if n%2==0:
 #           yield n
#for num in even_numbers(10):
#    print(num,end=" ")

def infinite_number():
    n=1
    while True:
        yield n
        n+=1
g=infinite_number()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
