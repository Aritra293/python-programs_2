n=int(input("enter the number of terms:"))
i=1
dummy_list=[]
while i<=n:
    value=input("enter some values separated by comma:")
    dummy_list.append(tuple(value.split(",")))
    i+=1
    print(dummy_list)
    
