print("1.Determinant of 2x2")
print("2.Determinant of 3x3")
print("3.Inverse of 2x2")
print("4.Inverse of 3x3\n")
o = int(input("Enter your choice: "))

def mo2(a):
    a11 = int(input("Enter a11: "))
    a12 = int(input("Enter a12: "))
    a21 = int(input("Enter a21: "))
    a22 = int(input("Enter a22: "))
    m   = [[a11,a12],[a21,a22]]
    

    d = a11*a22 - a21*a12
    if a==1: print(d)
    return [d,m]
    


def mo3(a):
    a11 = int(input("Enter a11: "))
    a12 = int(input("Enter a12: "))
    a13 = int(input("Enter a13: "))
    a21 = int(input("Enter a21: "))
    a22 = int(input("Enter a22: "))
    a23 = int(input("Enter a23: "))
    a31 = int(input("Enter a31: "))
    a32 = int(input("Enter a32: "))
    a33 = int(input("Enter a33: "))
    
    d = a11*(a22*a33-a32*a23)-a12*(a21*a33-a31*a23) + a13*(a21*a32-a31*a22)
    m = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
    if a==1: print(d)
    return [d,m]

def a1():
    x = mo2(2)
    d = x[0]
    if d ==0: return print("Inverse not exist as Determinant is 0")
        
    m = x[1]
    c ='1/{}'.format(d)

    m1 = [c+str([m[1][1],-(m[0][1])]),' '*len(c)+str([-(m[1][0]),m[0][0]])]
    for i in m1:
        print(i)    
            
def a2():
    x = mo3(2)
    d = x[0]
    if d ==0: return print("Inverse not exist as Determinant is 0")
    m = x[1]
    e ='1/{}'.format(d)
    a = m[0];b = m[1];c = m[2]

    j = [ [b[1],b[2],b[0],b[1]],
          [c[1],c[2],c[0],c[1]],
          [a[1],a[2],a[0],a[1]],
          [b[1],b[2],b[0],b[1]]
          ]
    f = j[0];k = j[1]
    l = j[2];n = j[3]   
    m2 = [[(f[0]*k[1]-k[0]*f[1]),(f[1]*k[2]-k[1]*f[2]),(f[2]*k[3]-k[2]*f[3])],
          [(k[0]*l[1]-l[0]*k[1]),(k[1]*l[2]-l[1]*k[2]),(k[2]*l[3]-l[2]*k[3])],
          [(l[0]*n[1]-n[0]*l[1]),(l[1]*n[2]-n[1]*l[2]),(l[2]*n[3]-n[2]*l[3])]
          ]
    q = m2[0];w = m2[1]
    s = m2[2]
    m3 = [' '*len(e)+str([q[0],w[0],s[0]]),
          e+str([q[1],w[1],s[1]]),
          ' '*len(e)+str([q[2],w[2],s[2]])
         ]                              
    for i in m3:
        print(i)

     


if   o == 1:mo2(1)
elif o == 2:mo3(1)
elif o == 3: a1()
elif o == 4: a2()    
    
    
