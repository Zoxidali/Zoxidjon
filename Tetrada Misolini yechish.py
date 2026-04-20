#27.09.2024 and 30.09.2024
#M-1
'''
# Tetrada soni
tetrada_soni = input("Tetrada sonini kiriting: ")

# Tetrada sonini o'nlik sanoq sistemasiga o'tkazish
onlik_son = int(tetrada_soni, 4)

print("O`nlik sanoq sistemasidagi qiymat:", onlik_son)
# O'nlik sonni ikkilik sanoq sistemasiga o'tkazish
ikkilik_son = bin(onlik_son)[2:]

# Natijani chop qilish
print("Ikkilik sanoq sistemasidagi qiymat:", ikkilik_son)
'''
#M-2
'''
# Ikkilik sanoq sistemasidagi son
ikkilik_soni = "10110111"

# Ikkilik sonini o'nlik sanoq sistemasiga o'tkazish
onlik_son = int(ikkilik_soni, 2)

print("O`nlik sanoq sistemasidagi qiymat:", onlik_son)

# O'nlik sonini to'rtlik sanoq sistemasiga o'tkazish
tetrada_soni = ""
if onlik_son == 0:
    tetrada_soni = "0"
else:
    while onlik_son > 0:
        tetrada_soni = str(onlik_son % 4) + tetrada_soni
        onlik_son //= 4

# Natijani chop qilish
print("To'rtlik sanoq sistemasidagi qiymat:", tetrada_soni)
'''
#M-3
'''
# 8 lik sanoq sistemasidagi son
sakkizlik_soni = "702"

# Sakkizlik sonini o'nlik sanoq sistemasiga o'tkazish
onlik_son = int(sakkizlik_soni, 8)

# O'nlik sonini ikkilik sanoq sistemasiga o'tkazish
ikkilik_son = bin(onlik_son)[2:]

# Natijani chop qilish
print("Ikkilik sanoq sistemasidagi qiymat:", ikkilik_son)
'''
#14likdan 2likka
'''
on_tortlik_soni = "AB"  

# 14-lik sonini o'nlik sanoq sistemasiga o'tkazish
onlik_son = int(on_tortlik_soni, 14)
print(onlik_son)
# O'nlik sonini ikkilik sanoq sistemasiga o'tkazish
ikkilik_son = bin(onlik_son)[2:]  

# Natijani chop qilish
print("Ikkilik sanoq sistemasidagi qiymat:", ikkilik_son)
'''
