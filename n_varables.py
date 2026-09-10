def add(*args):
    print(*args,end="")
    print(" length :=",len(args))
    return sum(args)

print(add(1,2,3,4,5 ))
print("Addition := ",add(1,2,3))
print("Addition := ",add(1,2,3,4,5,6))

def show(title,*names):
    print(f"title:={title}")
    print(f"names:={names}")
show("student","hemant","siddhi")

