def tag(tag, *args, **kwargs):
    if 'css' in kwargs:
        kwargs['class'] = kwargs.pop('css')
        # crio uma nova chave, e logo depois, usando o pop, pego o valor da chave 'css',
        # passo para a chave 'class', e excluo o conjunto chave e valor de 'css' e sua respectiva chave
    elif 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
        # veja o comentario acima
    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
