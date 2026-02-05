
# #Array1
# n= int(input("n= "))
# massiv= []
# #birinchi usul
# # for x in range( 0,n+1):
# #     if x%2!=0:
# #         massiv.append(x)
# # #ikkinchi usul
# # for x in range(1,n+1,2):
# #     massiv.append(x)
# print(massiv)

# #Array2
# n=int(input("n="))
# massiv=[]
# for x in range(n+1):
#     massiv.append(pow(2,x))
# print(massiv)

# #Array3
# n=int(input("n="))
# A=int(input("A="))
# D=int(input("D="))
# massiv=[]
# for x in range(n+1):
#     massiv.append(A)
#     A=A+D
# print(massiv)

# #Array4
# n=int(input("n="))
# A=int(input("A="))
# D=int(input("D="))
# massiv=[]
# for x in range(n+1):
#     massiv.append(A)
#     A=A*D
# print(massiv)

#Array5
n=int(input("n="))
F0= F1=1
massiv=[F0,F1]
F2=F0+F1
for x in range(n+1):
    F1,F2=F2,F1+F2
    massiv.append(F1)
print(massiv)
