def sayHello():
    print("...Executing the function")

def decorator(func):
    def inner():
        print("Before function call, Transaction initiated")
        func()
        print("After function call, Transaction completed")
    return inner

message = decorator(sayHello)
message()