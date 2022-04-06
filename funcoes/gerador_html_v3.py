def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'
    # nesta situação, conteudo é um parametro obrigatório enquanto classe é opcional
    # se nenhuma classe for definida, 'success' será fornecida por padrão.


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    # basicamente, um generator que vai fazer a concatenação de cada um dos itens da lista fornecida na string vazia
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
