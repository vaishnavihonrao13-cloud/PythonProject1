def check_role(role):
    def decorator(func):
        def wrapper(user_role):
            if role == user_role:
                print("Access granted")
                func(user_role)
            else:
                print("Access denied")
        return wrapper
    return decorator

@check_role("HR")
def view_salary(user_role):
    print("Display Employee Salary info")

view_salary("HR")
view_salary("employee")