def numeric():
    numbers = []
    orderned = False

    # Informar quantidade de numeros
    n = int(input('Quantidade de numeros: '))

    # Preencher lista de numeros
    for number in range(n):
        number = int(input(f'Numero #{number}: '))
        numbers.append(number)
    
    while not orderned:
        n = n - 1
        orderned = True
        for i in range(1, n):
            if numbers[i] > numbers[i+1]:
                aux = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = aux
                orderned = False

    print(numbers)

if __name__ == '__main__':
    # alphabetic()
    numeric()
