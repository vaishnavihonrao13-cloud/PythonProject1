from array import array
arr=array('i',[1,2,3,4,5,6,7,8,9])
#print(type(arr))
#print(arr)
val=arr.index(2)
#print(val)

a1=arr[:4]
#print(a1)
arr.remove(5)
#print(arr)

arr.append(10)
print(arr)

arr.insert(8,12)
print(arr)

