with open('numere1.txt', 'r') as f :
    a=f.readline()
    b=f.readline()
with open('minim1.txt','w') as f :
    if int(a)>int(b) :
        f.write(b)
    else: 
        f.write(a)