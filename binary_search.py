def pesquisa_binaria(lista, item):
    """
    Retorna o index de 'item' na 'lista', se nao achar, retorna None
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

def get_even_number(index: int) -> list:
    """
    Returns a list with all even numbers from '0' to 'index'
    """
    lista = []
    a = 0
    while a <= index:
        if a % 2 == 0:
            lista.append(a)
        a += 1
    return lista

a = get_even_number(6)
b = pesquisa_binaria(a, 6)

print(b)
