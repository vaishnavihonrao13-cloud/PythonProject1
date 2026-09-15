def div(a, b):
    print(a / b)
def smart_div(func):
    def wrapper(a,b):
        if a>b:
            func(a,b)
        else:
            func(b,a)
    return wrapper
div1= smart_div(div)
div1(2,4)
div1(4,2)

