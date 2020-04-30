# 1
'''a=0
for t in range (1,1000):
    if t%3==0 or t%5==0:
        a+=t
print(a)'''

#2
#3

'''a=int(input("Digit the number to calculate the prime factors:"))
b=2
while a!=1:
    if a%b==0:
        print(f"{a:<3}|",end=" ")
        a//=b
        print(b)
    b+=1
print(a)'''

# 4
'''a=0
for t in range (100,1000):
    for r in range (100,1000):
        if str(t*r)==str(t*r)[::-1] and t*r>a:
            a=t*r
print(a) yes'''

# 5
'''a=0
b=0
while b!=20:
    a+=1
    b=0
    for t in range (1,21):
        if a%t==0:
            b+=1
        else:
            break
print(a)'''

#6
'''a=0
for t in range (1,101):
    a+=t**2
b=0
for r in range (1,101):
    b+=r
b**=2
print(b-a)'''

#7
'''a=0
b=0
while a!=10001:
    d = 0
    b += 1
    for c in range (b,0,-1):
        if b%c==0:
            d+=1
    if d==2:
        a+=1
print(b)'''

#8
print("As minhas alteraçõeszinhas para ele..")
a=0
b=7
if a>b:

print("O programa está feito.")