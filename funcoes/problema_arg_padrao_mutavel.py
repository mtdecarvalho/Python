def fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default tem uma armadilha
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    # neste caso, ambos os objetos possuem o mesmo id, logo, são o mesmo objeto em memória.
    # por esse motivo não é recomendável utilizar objetos mutáveis como parametros padrões de funções
    print(restart, id(restart))
    assert restart == [0, 1, 1]
