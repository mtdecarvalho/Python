bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)
    # essa função retorna uma string concatenada com espaços com os atributos novos, porém
    # só concatenando os mesmos se eles estiverem presentes dentro da tupla de suportados,
    # logo se for passada a tupla bloco_atrs, apenas os elementos que estiverem dentro de
    # bloco_atrs serão concatenados na string.
    # para clarear, ele separa a chave bloco_accesskey e pega apenas o último índice (com o -1),
    # e depois pega sua chave, transformando "bloco_accesskey": "m" em accesskey="m"


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    # se conteudo não for uma função será atribuido a html, caso contrário o retorno da função conteudo será atribuida ao html
    atributos = get_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'
    # nesta situação, conteudo é um parametro obrigatório enquanto classe é opcional
    # se nenhuma classe for definida, 'success' será fornecida por padrão.


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    # basicamente, um generator que vai fazer a concatenação de cada um dos itens da lista fornecida na string vazia
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


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

    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='color: red'))
