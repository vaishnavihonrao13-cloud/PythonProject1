from prime import isPrime

for i in range(10):
    print(i,end="")
print()

for i in range(1,21,2):
    print(i,end="")
print()

for i in range(10,0,-1):
    print(i,end="")
print()

str='Python'
for ch in str:
    print(ch,end=",")
print()

str="Hello"
for ch in str:
    if ch=='l':
        print(ch,'found')
print()

for i in range(1,11):
    if i==5:
        continue
    print(i,end="")
print()

for i in range(1,6):
    print(i,end="")
else:
    print("loop complete")
print()

name = "Programming"
count = 0
for ch in name:
    if ch in "aeiou":
        count += 1
print('Total vowels := ', count)

print()

text = "Python"
reversed = ""
for ch in text:
    reversed = ch + reversed

print(reversed)

base=5
pow=1
for index in  range(4,0,-1):
    pow=pow*base
print("power:-",pow)
print()

num=51
isPrime=True
for i in range(2,num/2,1):
    if num%i==0:
        isPrime=False
        break
if isPrime:
    print("Prime number")
else:
    print("Not Prime number")