try:
    x=int(input("enter x:"))
    y=input("enter y:")
    print(x/y)
except ValueError:
    print("invalid integer")
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("invalid type")
