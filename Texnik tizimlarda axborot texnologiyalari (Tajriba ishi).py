'''
k=int(input(' Mahsulotni kilosini kiriting!   '))
u=0
p=int(input(f'{k} Kilo maxsulotni narxini kiriting!   '))
kunmah=int(input(' Maxsulotni kunlik sotilgan kilosini kiriting!   '))
s=p/k
for kun in range(1,31):
    x=(kunmah+kun)*s
    print(f'{kun}-kuni {x}so`mlik mahsulot sotildi!')
    u=u+x
print(f'Umumiy {u} so`mlik mahsulot sotildi!')
'''
'''
n=int(input('N='))
c=0
for x in range (2,n):
    if n%x==0:
        c=c+1
if c==0:
    print("Tub son")
else:
    print('Tub son emas')
'''
'''
y=int(input('Yilni kiriting! '))   
if y%400==0 :
    print('Kabisa yili')
elif y%100==0:
    print('kabisa yili emas')
elif y%4==0:
    print('kabisa yili')
'''
'''
n = int(input(" Enter n:  "))
r1 = n % 10
r10 = n // 10 % 10
r100 = n // 100 % 10
r1000 = n // 1000%10
r10000=n//10000%10
r100000=n//100000
if r100000 == 1:
    print("Bir yuz")
elif r100000 == 2:
    print("Ikki yuz")
elif r100000 == 3:
    print("Uch yuz")
elif r100000 == 4:
    print("To'rt yuz")
elif r100000 == 5:
    print("Besh yuz")
elif r100000 == 6:
    print("Olti yuz")
elif r100000 == 7:
    print("Yetti yuz")
elif r100000 == 8:
    print("Sakiz yuz")
elif r100000 == 9:
    print("To'qqiz yuz")
if r10000 == 1:
    print("O`n")
elif r10000 == 2:
    print("Yigirma ")
elif r10000 == 3:
    print("O`ttiz ")
elif r10000 == 4:
    print("Qirq ")
elif r10000 == 5:
    print("Ellik ")
elif r10000 == 6:
    print("Oltmish ")
elif r10000 == 7:
    print("Yetmish ")
elif r10000 == 8:
    print("Sakson ")
elif r10000 == 9:
    print("To'qson ")
if r1000 == 1:
    print("Bir ming")
elif r1000 == 2:
    print("Ikki ming")
elif r1000 == 3:
    print("Uch ming")
elif r1000 == 4:
    print("To'rt ming")
elif r1000 == 5:
    print("Besh ming")
elif r1000 == 6:
    print("Olti ming")
elif r1000 == 7:
    print("Yetti ming")
elif r1000 == 8:
    print("Sakiz ming")
elif r1000 == 9:
    print("To'qqiz ming")
if r100 == 1:
    print("Bir yuz")
elif r100 == 2:
    print("Ikki yuz")
elif r100 == 3:
    print("Uch yuz")
elif r100 == 4:
    print("To'rt yuz")
elif r100 == 5:
    print("Besh yuz")
elif r100 == 6:
    print("Olti yuz")
elif r100 == 7:
    print("Yetti yuz")
elif r100 == 8:
    print("Sakiz yuz")
elif r100 == 9:
    print("To'qqiz yuz")
if r10 == 1:
    print("O'n")
elif r10 == 2:
    print("Yigirma")
elif r10 == 3:
    print("O'ttiz")
elif r10 == 4:
    print("Qirq")
elif r10 == 5:
    print("Ellik")
elif r10 == 6:
    print("Oltmish")
elif r10 == 7:
    print("Yetmish")
elif r10 == 8:
    print("Sakson")
elif r10 == 9:
    print("To'qson")
if r1 == 1:
    print("Bir")
elif r1 == 2:
    print("Ikki")
elif r1 == 3:
    print("Uch")
elif r1 == 4:
    print("To'rt")
elif r1 == 5:
    print("Besh")
elif r1 == 6:
    print("Olti")
elif r1 == 7:
    print("Yetti")
elif r1 == 8:
    print("Sakkiz")
elif r1 == 9:
    print("To'qqiz")
'''
'''
z=int(input('Nechinchi oyligini! '))
if z %2==1 and z<7 or z==8 :
    print("31 kunlik")
elif z %2==0 and z!=2  :
    print("30 kunlik")
if z==2:
    k=input('kabisa yilimi? ')
    if k=="ha":
        print('29 kunlik')
    else:
        print('28 kunlik')
'''
'''
d=int(input('kunni kiriting! '))
m=int(input('oyni kiriting'))
r1=d%10
r10=d//10%10
if r1==1:
    kun='birinchi'
elif r1==2:
    kun='ikkinchi'
elif r1==3:
    kun='uchinchi'
elif r1==4:
    kun='to`rtinchi'
elif r1==5:
    kun='beshinchi'
elif r1==6:
    kun='oltinchi'
elif r1==7:
    kun='yettinchi'
elif r1==8:
    kun='sakkizinchi'
elif r1==9:
    kun='to`qqizinchi'
if r10==1:
    on='o`n'
elif r10==2:
    on='yigirma'
elif r10==3:
    on='o`ttiz'
else:
    on=''
if m==1:
    oy='yanvar'
elif m==2:
    oy='fevral'
elif m==3:
    oy='mart'
elif m==4:
    oy='aprel'
elif m==5:
    oy='may'
elif m==6:
    oy='iyun'
elif m==7:
    oy='iyul'
elif m==8:
    oy='avgust'
elif m==9:
    oy='sentabr'
elif m==10:
    oy='oktabr'
elif m==11:
    oy='noyabr'
elif m==12:
    oy='dekabr'
print(on ,kun,oy)
'''
'''
z=input("Robot qaysi tomonga qarab turibdi? ")
k=int(input("Burilish uchun raqamni tanlang! \n 1. o'ng \n 2. chap \n 3.Xech qayerga burilmaydi. \n"))
if k==1 and z=="Shimol":
    print(f"{z} tomondan Sharq tomonga burildi! ")
elif k==2 and z=="Shimol":
    print(f"{z} tomondan G'arb tomonga burildi!")
if z=="Janub" and k==1:
    print(f"{z} tomondan G'arb tomonga burildi! ")
elif z=="Janub" and k==2:
    print(f"{z} tomondan Sharq tomonga burildi! ")
if z=="G'arb" and k==1:
    print(f"{z} tomondan Shimol tomonga burildi! ")
elif z=="G'arb" and k==2:
    print(f"{z} tomondan Janub tomonga burildi! ")
if z=="Sharq" and k==1:
    print(f"{z} tomondan Janub tomonga burildi! ")
elif z=="Sharq" and k==2:
    print(f"{z} tomondan Shimol tomonga burildi! ")
elif z=="{z}" and k!=1 or k!=2:
    print(f"{z} tomondan o'zgarmadi!")

'''
'''
z=10#kilometr
x=0
q=0
while x<200:#kilometr
    z=(7*z)/100+z
    x=x+z
    q=q+1
print(q,'-kun',x,'km')
'''
'''
N=int(input("N="))
a=1
while a<N:
    a=3*a
print(N==a)    
'''
'''
n=int(input("N= "))
s=0
q=0
z=0
while n!=0:
    q=n%10
    s=s+q
    n=n//10
    z=z+1
print(z, "xona sonning yig'indisi",s)
'''
#Uyga Vazifa
# n berilgan son Fibonatchi sonimi?

n=int(input ("N sonini kiritng! "))
c=0
a=1
b=1
#if n==1:
 #   print("Bu Fibonacci soni! ")
#else:
while c<n:
    c= a+b
    a=b
    b=c
    print(v)
#    if c==n:
#        print("Bu Fibonacci soni! ")
#    else :
#        print("Bu Fibonacci soni emas! ")

# 10.11.2023y
# Massivda doimo elementlarni aniq belgilab olamiz.
#Mavzu: Listlar. Pythonda massivlar bilan ishlash.  
#Pythonda listlar . masalan:L=[1,5,8,0,-8,0,7,4,br,brr]
#L=[1,2,3,4,5,6,7,8,9]
# slicing-qirqib olish, parrak 
#print(L[ : ])
'''
L=['nok','olma','nok','olma','nok','nok','olma','nok','olma']
k=len(L)
n=0
o=0
for x in range (k):
    if L[x] == 'nok':
        n=n+1
    else:
        o=o+1
print(n,' ta nok' ,'\n', o ,'ta olma ')
'''

    



























