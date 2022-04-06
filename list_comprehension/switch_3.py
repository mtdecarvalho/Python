def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia de Semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    # a linha acima é um generator do dia escolhido, que será gerado a partir dos números de dias (de 1 até 7)
    # e os respectivos tipos de dia (fim de semana ou dia de semana) e retornará um tipo de dia
    # caso o número do dia passado esteja incluso nos numeros. no caso de erro, é retornado '** dia invalido **'.
    return next(dia_escolhido, '** dia invalido **')

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')