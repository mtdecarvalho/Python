dobro_dos_pares = [ i * 2 for i in range(10) if i % 2 == 0 ]
print(dobro_dos_pares)

dobro_dos_impares = [ i * 2 for i in range(10) if i % 2 != 0 ]
print(dobro_dos_impares)


# "normal"
pares, impares = [], []
for i in range(10):
    if i % 2 == 0:
        pares.append(i * 2)
    else:
        impares.append(i * 2)
print(pares, impares)