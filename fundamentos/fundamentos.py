# OPERADORES ARITMETICOS 

'''
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3)
print(2 ** 8)
print(10 % 3)
'''

# OPERADORES RELACIONAIS

'''
3 > 4
4 >= 3
1 < 2
3 <= 1
3 != 2
3 == 3
2 == '2'
'''

# OPERADORES DE ATRIBUICAO 

'''
a = 3
a = a + 7

a += 5

a -= 3 

a /= 4

a %= 4

a **= 8

a //= 256
'''

# OPERADORES LOGICOS

'''
TABELA VERDADE DO AND

True and True = 1
True and False = 0
False and True = 0
False and False = 1

TABELA VERDADE DO OR

True and True = 1
True and False = 1
False and True = 1
False and False = 0

TABELA VERDADE DO XOR 

True and True = 0
True and False = 1
False and True = 1
False and False = 0

OPERADOR DE NEGACAO

not True
not False

'''

# OPERADORES UNARIOS

'''
a++ e a-- nao sao suportados
a += 3
a -= 3
'''

#   OPERADORES TERNARIOS

'''
esta_chuvendo = True

print('Hoje minhas roupas estao ' + ('secas.', 'molhadas.')[esta_chuvendo])
print('Hoje minhas roupas estao ' + ('molhadas.' if esta_chuvendo else 'secas.'))
'''

# OPERADOR DE MEMBRO

'''
lista = [1, 2, 3, 'Ana', 'Carla']
print( 2 in lista )
print( 'Ana' not in lista )
'''

# OPERADOR DE IDENTIDADE

'''
x = 3
y = x 
z = 3

print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
'''

#   CONVERSAO DE TIPOS

'''
2 + 3
'2' + '3'


a = 2 
b = '3'

print(type(a))
print(type(b))
print(a + int(b))
print(str(a) + b)

print(type(str(a)))

# print(2 + int('2 legal'))

print(2 + float('3.4'))
'''

#   COERCAO AUTOMATICA

'''
print(type(10 / 2))
print(type(10 // 3))
print(type(10 // 3.3))
print(2 + True)
print(2 + False)
print(type(1 + 2))
print(type(1 + 2.5))
'''

#   TIPOS NUMERICOS

'''
a = 5
b = 2.5
print(type(a))
print(type(a / b))
print(type(b))
print(type(a - b))

print(b.is_integer())
print(5.0.is_integer())
print(abs(-2))
print(abs(-3.5))


from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))

getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))
'''

# STRINGS

'''
nome = 'Saulo Pedro'
print(nome)
print(nome[0])

print('marca d\'agua')
print("marca d'agua")
print('Texto entre apostrofos pode ter "aspas"')

doc = """Texto com multiplas
    ... linhas"""
print(doc)
print("Texto com multiplas\n\t... linhas")
'''
# print('''Tambem eh possivel com
#  ...3 aspas simples''')
'''
nome = "Ana Paula"
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])
print(nome[::-1])

numeros = '1234567890'
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])

frase = 'Python eh uma linguagem excelente'

print('py' not in frase)
print('ing' in frase)
print(len(frase))

print(frase.lower())
print(frase.upper())

frase = frase.lower()
print(frase)

frase = frase.upper()
print(frase)

print(frase.split())
print(frase.split('E'))


a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))

print(len(a))
print(a.__len__())

print('1' in a)
print(a.__contains__('1'))
'''

#   LISTAS

'''
lista = [] 
print(type(lista))
print(len(lista))

lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)

nova_lista.remove(5)
print(nova_lista)

nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme'))
print(lista[2])
print(1 in lista)
print("Rebeca" in lista)
print('Pedro' in lista)
print(lista[0])
print(lista[4])
print(lista[-1])
print(lista[-5])

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])

del lista[2]
print(lista)
del lista[1:]
print(lista)
'''

#   TUPLAS

'''
tupla = tuple()
tupla = ()
print(type(tupla))

tupla = ('um')
print(type(tupla))

tupla = ('um',)
print(type(tupla))

print(tupla[0])
# tupla[0] = 'novo'

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))

print(len(cores))
'''

#   DICIONARIOS

'''
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Ingles', 'Portugues']}
print(type(pessoa))
print(len(pessoa))

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))

pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa)

pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)

pessoa.pop('idade')
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)
'''

#   SET

'''
a = {1, 2, 3}
print(type(a))

a = set('cod3r') 
print(a)

a = set('codddddd3r')
print(a)

print('3' in a, 4 not in a)

print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))
print(c1.intersection(c2))

c1.update(c2)
print(c1)

print(c2 <= c1)
print(c1 >= c2)

print({1, 2, 3} - {2})

print(c1 - c2)

c1 -= {2}
print(c1)
'''

#   INTERPOLACAO

from string import Template

nome, idade = 'Ana', 30

print("Nome: %s Idade: %d" % (nome, idade)) # MAIS ANTIGA
print("Nome: {0} Idade: {1}".format(nome, idade)) # PYTHON < 3.6
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))