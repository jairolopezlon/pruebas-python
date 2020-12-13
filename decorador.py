def probar(fun):
    def inside(x, y):
        if y > x:
            print('saldra un valor negativo')
            return
        return fun(x, y)
    return inside


@probar
def resta(x, y):
    return x - y


print(resta(44, 8))
