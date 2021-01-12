with open('input.txt', 'r') as f: 
    n=f.readline()
    n1= int(n)-2
    n2= int(n)-1
    n3= int(n)+1
    n4= int(n)+2
with open('output.txt', 'w') as f:
    f.write(str(n1))
    f.write(' ')
    f.write(str(n2))
    f.write(' ')
    f.write(str(n)) 
    f.write(' ')
    f.write(str(n3))
    f.write(' ')
    f.write(str(n4))