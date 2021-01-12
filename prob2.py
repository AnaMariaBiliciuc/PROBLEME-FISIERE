with open('numere.txt', 'r') as f:
    a=f.readline()
    b=f.readline()
if int(a)> int(b) :
     x= int(a)*2
     y= int(b)*3
else :
     x=int(b)*2 
     y=int(a)*3
with open('produs.txt', 'w') as f :
    f.write(str(x))
    f.write(' ')
    f.write(str(y))
 