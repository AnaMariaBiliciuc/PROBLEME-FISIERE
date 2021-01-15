with open('numar.txt', 'r') as f:
    a=f.read()
x1= int(a)*1
x2= int(a)*2
x3= int(a)*3
x4= int(a)*4
x5= int(a)*5
x6= int(a)*6
x7= int(a)*7
x8= int(a)*8
x9= int(a)*9
x10= int(a)*10
n1= '1*'+ str(a)+'='+str(x1)
n2= '2*'+ str(a)+'='+str(x2)
n3= '3*'+ str(a)+'='+str(x3)
n4= '4*'+ str(a)+'='+str(x4)
n5= '5*'+ str(a)+'='+str(x5)
n6= '6*'+ str(a)+'='+str(x6)
n7= '7*'+ str(a)+'='+str(x7)
n8= '8*'+ str(a)+'='+str(x8)
n9= '9*'+ str(a)+'='+str(x9)
n10= '10*'+ str(a)+'='+str(x10)
with open ('inmultire.txt', 'w') as f:
    f.write(str(n1))
    f.write('\n')
    f.write(str(n2))
    f.write('\n')
    f.write(str(n3))
    f.write('\n')
    f.write(str(n4))
    f.write('\n')
    f.write(str(n5))
    f.write('\n')
    f.write(str(n6))
    f.write('\n')
    f.write(str(n7))
    f.write('\n')
    f.write(str(n8))
    f.write('\n')
    f.write(str(n9))
    f.write('\n')
    f.write(str(n10))
    f.write('\n')
