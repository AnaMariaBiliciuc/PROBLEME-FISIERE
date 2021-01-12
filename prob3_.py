with open('globulet.txt', 'r') as f:
    a1=f.readline()         #globulete albe
    r= int(a1) +3            #calculeaza nr de globulete rosii
    s1= int(a1) +r           #suma blobulete albe si rosii
    a2= s1 -2               #calculeaza nr de globulete albastre
    s2= int(a1)+r+a2        #suma totala de globulete
with open('bradut.txt', 'w') as f:
    f.write(str(s2))