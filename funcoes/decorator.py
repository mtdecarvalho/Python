# um decorator consiste em literalmente decorar um objeto, adicionando funcionalidades antes e depois do mesmo.

def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada da funcao: {resultado}')
        return resultado
    return decorator
# este decorator retornará todos os argumentos passados para a função bem como o resultado da mesma e rodará também os próprios procedimentos


@log # define o decorator de soma
def soma(x, y):
    return x + y


@log # define o decorator de sub
def sub(x, y):
    return x - y

if __name__ == '__main__':
    print(soma(5,7))
    print(sub(5, y=7))
