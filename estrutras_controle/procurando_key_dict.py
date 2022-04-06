def get_keys(dicionario, valor):
    

    listOfKeys = list()
    listofitems = dicionario.items()


    for i in listofitems:
        if i[0] == valor:
            listOfKeys.append(i[0])
    return listOfKeys

dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terca',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }


listOfKeys = get_keys(dias, 3)


for key in listOfKeys:
    print(key)