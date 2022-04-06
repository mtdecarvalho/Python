def tag_bloco(texto, classe='success'):     
    return f'<div class="{classe}">{texto}</div>' 
    # nesta situação, texto é um parametro obrigatório enquanto classe é opcional
    # se nenhuma classe for definida, 'success' será fornecida por padrão.

if __name__ == '__main__':
    # Testes (assertions)
    # assertions são testes que são realizados em uma função e que em caso de falha
    # retornam AssertionError
    assert tag_bloco("Incluído com sucesso!") == \
        '<div class="success">Incluído com sucesso!</div>'
    assert tag_bloco("Impossível excluir!", 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
