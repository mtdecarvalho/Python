def get_tipo_dia(valor):
    semana = {
        1: 'Fim de semana',
        2: 'Dia util',
        3: 'Dia util',
        4: 'Dia util',
        5: 'Dia util',
        6: 'Dia util',
        7: 'Fim de semana'
    }
    return semana.get(valor, "** INVALIDO **")

if __name__ == '__main__':
    for i in range(8):
        print(f'{i}: {get_tipo_dia(i)}')