tup=()
print(tup)
#using string
tup=('hi','hi')
print(tup)
#using list
li=[1,2,3,4]
print(tuple(li))
#using built-in function
tup=tuple('hello')
print(tup)
#search element by indexing
tup=(1,2,3,4)
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[:3])
print(tup[3:])
print(len(tup))
# unpacking of tuple
student=("vaishnavi",21,99)
name,age,marks=student
print("name",name)
print("age",age)
print("marks",marks)
# sum of elements
nums=(22,3,4,5,6)
sum=0
for n in nums:
    sum+=n
print("sum",sum)
