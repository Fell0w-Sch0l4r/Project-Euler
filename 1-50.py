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
print(a)'''

# 5    232792560
a=0
b=0
while b!=20:
    a+=1
    b=0
    for t in range (1,21):
        if a%t==0:
            b+=1
print(a)