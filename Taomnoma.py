#Buyurtma
print('Assalomu aleykum! Restarauntimizga Xush kelibsiz')
print('Marhamat bizning menu bilan tanishing')
print(' 1. Osh','\n' , ' 2.sho`rva','\n' , '3.grechka','\n' ,'4. somsa','\n' ,'5. dimlama')
taom=int(input('Nima buyurasiz? Raqamni tanlang! '))
if taom==1:
    print('Marhamat oshni qabul qilib oling')
    print('1portsa osh 25 ming')
    portsa=float(input('Qancha osh buyurasiz? '))
    print(f' Marhamat siz {portsa*25000} so`m to`lovni amalga oshiring ')
    print(' Siz salat, non yoki choy hohlaysizmi? choy 3 ming, salat 7 ming, non esa 3 ming so`m ')
    choy=input(' Agar choy hohlasangiz olib kelaymi? ')
    if choy=='ha':
        print(f' Marhamat siz {(portsa*25000)+3000} so`m to`lovni amalga oshiring ')
    else:
        print(f' Tashrifingiz uchun raxmat! Marhamat siz {portsa*25000} so`m to`lovni amalga oshiring ')
    salat=input('Agar salat hohlasangiz olib kelaymi? ')
    if salat=='ha':
        print(f' Marhamat siz {(portsa*25000)+7000+3000} so`m to`lovni amalga oshiring ')
    else:
        print(f' Tashrifingiz uchun raxmat! Marhamat siz {(portsa*25000)+3000} so`m to`lovni amalga oshiring ')
    non=input(' Agar non hohlasangiz olib kelaymi? ')
    if non=='ha':
        non=float(input('Nechta non olasiz? '))
        print(f' Marhamat siz non uchun {non*3000} to`lovni amalga oshiring')    
        print(f' Marhamat siz umumiy {(non*3000)+(portsa*25000)+3000+7000}  so`m to`lovni amalga oshiring ')
    else:
        print( f' Tashrifingiz uchun raxmat')
        print(f' Tashrifingiz uchun raxmat! Siz umumiy {(portsa*25000)+3000+7000} so`m to`lovni amalga oshiring ')
'''
elif taom==2:
    print('Marhamat sho`rvani qabul qilib oling')
    print('1portsa sho`rva 15 ming')
    portsa=float(input('Qancha sho`rva buyurasiz? '))
    print(f' Marhamat siz {portsa*15000} so`m to`lovni amalga oshiring ')
    print(' Siz salat, non yoki choy hohlaysizmi? choy 3 ming, salat 7 ming, non esa 3 ming so`m ')
    choy=input(' Agar choy hohlasangiz olib kelaymi? ')
    if choy=='ha':
        print(f' Marhamat siz {(portsa*15000)+3000} so`m to`lovni amalga oshiring ')
    else:
        print(f'Tashrifingiz uchun raxmat! Marhamat siz {portsa*15000} so`m to`lovni amalga oshiring ')
    salat=input('Agar salat hohlasangiz olib kelaymi? ')
    if salat=='ha':
        print(f' Marhamat siz {(portsa*15000)+3000+7000} so`m to`lovni amalga oshiring ')
    else:
        print(f'Tashrifingiz uchun raxmat! Marhamat siz {(portsa*15000)+3000} so`m to`lovni amalga oshiring ')
    non=input(' Agar non hohlasangiz olib kelaymi? ')
    if non=='ha':
        non=float(input('Nechta non olasiz? '))
        print(f' Marhamat siz non uchun {non*3000} to`lovni amalga oshiring')    
        print(f' Marhamat siz umumiy {(non*3000)+(portsa*15000)+3000+7000}  so`m to`lovni amalga oshiring ')
    else:
        print(f' Tashrifingiz uchun raxmat! Siz umumiy {(portsa*15000)+3000+7000} so`m to`lovni amalga oshiring ')
        
elif taom==3:
       print('Marhamat grechkani qabul qilib oling')
        print('1portsa grechka 30 ming')
    portsa=float(input('Qancha osh buyurasiz? '))
    print(f' Marhamat siz {portsa*30000} so`m to`lovni amalga oshiring ')
    print(' Siz salat yoki choy hohlaysizmi? choy 3 ming salat esa 7 ming so`m ')
    choy=input(' Agar choy hohlasangiz olib kelaymi? ')
    if choy=='ha':
        print(f' Marhamat siz {25000+3000} so`m to`lovni amalga oshiring ')    
    salat=input('Agar salat hohlasangiz olib kelaymi? ')
    if salat=='ha':
        print(f' Marhamat siz {25000+3000+7000} so`m to`lovni amalga oshiring ')
        print(' Tashrifingiz uchun raxmat! ')
    else:
        print('Tashrifingiz uchun raxmat! ')
elif taom==4:
       print('Marhamat somsani qabul qilib oling')
        print('1portsa somsa 10 ming')
    portsa=float(input('Qancha osh buyurasiz? '))
    print(f' Marhamat siz {portsa*10000} so`m to`lovni amalga oshiring ')
    print(' Siz salat yoki choy hohlaysizmi? choy 3 ming sous esa tekin ')
    choy=input(' Agar choy hohlasangiz olib kelaymi? ')
    if choy=='ha':
        print(f' Marhamat siz {25000+3000} so`m to`lovni amalga oshiring ')    
    sous=input('Agar sous hohlasangiz olib kelaymi? ')
    if sous=='ha':
        print(f' Marhamat siz {25000+3000} so`m to`lovni amalga oshiring ')
        print(' Tashrifingiz uchun raxmat! ')
    else:
        print('Tashrifingiz uchun raxmat! ')
       
else:
       print('Marhamat dimlamani qabul qilib oling')
        print('1 portsa dimlama 20 ming')
    portsa=float(input('Qancha osh buyurasiz? '))
    print(f' Marhamat siz {portsa*20000} so`m to`lovni amalga oshiring ')
    print(' Siz salat yoki choy hohlaysizmi? choy 3 ming salat esa 7 ming so`m ')
    choy=input(' Agar choy hohlasangiz olib kelaymi? ')
    if choy=='ha':
        print(f' Marhamat siz {25000+3000} so`m to`lovni amalga oshiring ')    
    salat=input('Agar salat hohlasangiz olib kelaymi? ')
    if salat=='ha':
        print(f' Marhamat siz {25000+3000+7000} so`m to`lovni amalga oshiring ')
        print(' Tashrifingiz uchun raxmat! ')
    else:
        print('Tashrifingiz uchun raxmat! ')
'''        


