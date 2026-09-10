name=["vaishanvi","siddhi"]
name.append("shruti")
print(name)
name.remove("siddhi")
#print(name)
#name.pop()
print(name)
name.sort()
print(name)
name.sort(reverse=True)
print("largest :",name[0])
print("smallest :",name[-1])
#withouut sort
li = [10, 25, 7, 45, 18]
greatest = li[0]
for i in li:
    if i > greatest:
        greatest = i
print("Greatest =", greatest)
unique = []
frequency = []
for i in li:
    if i not in unique:
        unique.append(i)
        frequency.append(li.count(i))
print("not duplicate:", unique)
print("Frequency:", frequency)
small = li[0]
second = li[0]
for i in range(1,len(li)):
    if small>li[i]:
        second=small
        small=li[i]
print("2nd smallest =", second)