def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    # se conteudo não for uma função será atribuido a html, caso contrário o retorno da função conteudo será atribuida ao html
    return f'<{tag} class="{classe}">{html}</{tag}>'
    # nesta situação, conteudo é um parametro obrigatório enquanto classe é opcional
    # se nenhuma classe for definida, 'success' será fornecida por padrão.


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    # basicamente, um generator que vai fazer a concatenação de cada um dos itens da lista fornecida na string vazia
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    # como neste caso tag_lista é uma função e a função usa *args, 
    # se torna necessário usar parâmetros nomeados para que eles não sejam passados como itens da função,
    # o que pode ser observado na linha abaixo. 
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', 'info', True))
