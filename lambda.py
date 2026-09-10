square = lambda x: x * x
print("square:", square(10))

swap=lambda a,b:(b,a)
a=10
b=20
a,b=swap(a,b)
print("a:", a)
print("b:", b)

max=lambda a,b:a if a>b else b
print(max(20,16))

