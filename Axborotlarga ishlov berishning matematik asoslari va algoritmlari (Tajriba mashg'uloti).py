'''
#2-mavzu
#5
print('Assalomu aleykum')
ism=int(input(' Yoshingizni kiriting=  '))
if 18< ism<30 :
    print('Siz 1- guruhga qabul qilindingiz!')
elif 31< ism <40 :
    print('Siz 2- guruhga qabul qilindingiz!')
elif 41< ism <50 :
    print('Siz 3- guruhga qabul qilindingiz!')
else:
    print('Uzur sizning yoshingiz kattaligi uchun ishga qabul qilinmadingiz!')
'''
'''
#14
import math
x=int(input('x='))
a=4
b=3
e=2.71
if x<1:
    print(6*x-a*x**2+math.cos(x))
elif x==1:
    print(math.sqrt(x**2+e**(-2))*abs(x))
elif x>1:
    print(e**b*x *abs(15-x**2)+b)
else:
    print('yechim yo`q!')
'''
'''
#9
m=int(input('shirinlik ='))
if m==1:
    print('Mahsulotda 5% shakar bor!')
elif m==2:
    print('Mahsulotda 7% shakar bor!')
elif m==3:
    print('Mahsulotda 8% shakar bor!')
else:
    print('Bunday turdagi shirinlik yo`q!')
'''
'''
#3-Mavzu
#5
c=0
for x in range(40,101):
    if x<101:
        c=c+40
print(c)    

#24
c=0
for x in range(1,29):
    if x%7==0:
        c=c+x
print(c)
'''
'''
#Mavzuda berilgan masalalar to'plami
#3
a=int(input('a='))
b=int(input('b='))
if a>0 and b>0 :
    print(a+b)
'''
# 11.11.2023  Mavzu:Pyhtonda  to'plamlar b/n ishlash

#num_set = set([1, 2, 3, 1, 2]) 
#print(num_set)

#months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", 
#"Nov", "Dec"])
#for m in months: 
# print(m)

#months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
#months.add("Feb")
#print(months)


#num_set = {1, 2, 3, 4, 5, 6} 
#num_set.remove(3) # remove() or discard()
#print(num_set)


#1- topshiriq
'''
a=set("Salom dunyo")
b=set("Hello World")
for x in a,b:
    print(x)
'''
#2- topshiriq
'''
a=set("Salom dunyo")
b=set("Hello World")
print(a&b)
'''
#3-topshiriq
'''
a=set([1,5,5,4,3,2,9])
b=set([9,8,3,7,2,4,2,7,5,4])
print(a^b)
'''
#4-topshiriq

a=(['A, B, C, D, E, F, G, H, I,J,K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'])
print(a['A''K'])











