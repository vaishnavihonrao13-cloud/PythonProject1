def validate_age(func):
    def inner(age):
        if age >=18:
            return func(age)
        else:
            print("age is too young")
    return inner
@validate_age
def vote(age):
    print("eligiable" )

vote(18)
vote(16)
