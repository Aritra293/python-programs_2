file1=open("abcd.txt","r")
file2=open("xyz.txt","w")
while True:
    line=file1.readline()
    if(line==""):
        break
    words=line.split()
    words.reverse()
    str1=" "
    str2=str1.join(words)
    file2.write(str2+"\n")
    file2.close()
    file1.close()
