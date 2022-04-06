import sys
import errno



def nota_conceito(valor):
    if not valor.isdigit():
        print("Insira um numero.")
        sys.exit(errno.EINVAL)


    nota = float(valor)


    if nota > 10:
        return 'Nota invalida'
    elif 9.1 <= nota:
        return 'A'
    elif 8.1 <= nota:
        return 'A-'
    elif 7.1 <= nota:
        return 'B'
    elif 6.1 <= nota:
        return 'B-'
    elif 5.1 <= nota:
        return 'C'
    elif 4.1 <= nota:
        return 'C-'
    elif 3.1 <= nota:
        return 'D'
    elif 2.1 <= nota:
        return 'D-'
    elif 1.1 <= nota:
        return 'E'
    elif 0 <= nota:
        return 'E-'
    else: 
        return 'Nota invalida'


if __name__ == '__main__':
    valor_informado = input("Insira a nota do aluno: ")
    conceito = nota_conceito(valor_informado)
    print(conceito)
