#!/usr/bin/python
#Solution to problem at https://code.google.com/codejam/contest/351101/dashboard#s=p2
f=open(r"C:\Users\Desktop\C-large-practice.in","r") # Input file
fo=open(r"C:\Users\Desktop\hi.txt","w") # Output file
no_test_cases=int(f.readline()) #to read the number of test cases.
t9dict={'\n':'\n',' ':'0','a':'2','b':'22',\
        'c':'222','d':'3','e':'33','f':'333',\
        'g':'4','h':'44','i':'444','j':'5',\
        'k':'55','l':'555','m':'6','n':'66',\
        'o':'666','p':'7','q':'77','r':'777',\
        's':'7777','t':'8','u':'88','v':'888',\
        'w':'9','x':'99','y':'999','z':'9999'}
count=0 ## a counter 
for line in f :
    count+=1
    prev=line[0] #Store the previous entry to check if a space has to be given
    fo.write("Case #"+str(count)+": ")
    for i in line:
        if(t9dict[i][-1]==t9dict[prev][-1]): #add a space if previous letter is same as the current one
            fo.write(' '+t9dict[i])       
        else:                           #write into the output file without adding a space if the prev entry is different
            fo.write(t9dict[i])          
        prev=i
fo.close()
  
  
