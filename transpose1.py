a=[]
b=[]
print("\ninput for matrix 1\n")
m=int(input("enter rows:  "))
n=int(input("enter columns:  "))
for j in range(m): 
    a.append([])
    for i in range(n):
        a[j].append(input("enter value:"))

    for j in range(n): 
        b.append([])
        for i in range(m):
            b[j].append(a[i][j])

print("\nOriginal Matrix")
for j in range(m): 
    for i in range(n):
      print(a[j][i],end="\t")
    print("\n")

print("\nMatrix Transpose")
for j in range(n): 
    for i in range(m):
         print(b[j][i],end="\t")
    print("\n")
