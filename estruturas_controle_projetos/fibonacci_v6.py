def fibonacci(quantidade):
    resultado = [0, 1]
    while quantidade > len(resultado):
        resultado.append(sum(resultado[-2:]))
        # if quantidade == len(resultado):
            # break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)