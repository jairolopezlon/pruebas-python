datos1 = [45, -6, 2, 6, -2, -12, -6, -7, -45]
datos2 = [45, 6, -2, 6, -2, -12, -6, -7, -45]
datos3 = [45, 15, 56, 212, 52, 32, -15]


def masCercano(data):
    numMasCercano: int = data[0]

    for num in data:
        if numMasCercano == num:
            continue
        elif abs(numMasCercano) == abs(num):
            numMasCercano = abs(num)
        elif abs(numMasCercano) > abs(num):
            numMasCercano = num

    return numMasCercano


def main():

    # caso dos menores duplicados, pero uno es negativo
    print(masCercano(datos1))

    # caso los dos menores son negativos
    print(masCercano(datos2))

    # caso dos menores, pero uno es positivo y otro negativo
    print(masCercano(datos3))


if __name__ == '__main__':
    main()
