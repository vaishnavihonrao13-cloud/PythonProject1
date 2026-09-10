m=[]
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(j)
print(m)

# user input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Enter element: "))
        row.append(value)
    matrix.append(row)
print("Matrix:")
for i in matrix:
    print(i)

#compersion
m=[[c for c in range(3) ] for r in range(3)]
print(m)