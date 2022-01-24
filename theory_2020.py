#q2
#list =["Godavari","Kaveri","Krishna"]
#list.append("Narmada")
#print(list)
#list[0]="Tapti"
#print(list)

#q4
#string ="hello world"
#print(string[1:4])

#q3
#r=float(input("enter radius:"))
#area=3.14*r*r
#p=2*3.14*r
#print("area",area)
#print("perimeter",p)

# User input for number of rows 
def triangle(n):
    k=n-1
    for i in range(0,n):
# Inner loop will print number of Astrisk 
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end =" ")
        print("\r")
    n = 5
    triangle(n)
