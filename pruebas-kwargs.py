class Modelo():
    def __init__(self, **args):
        for arg in args:
            setattr(self, arg, args[arg])


class Animal(Modelo):
    color: str
    edad: int
    pais: str


newList = Animal(**{'color': 'amarillo', 'edad': 34, 'pais': 'chile'})

print(newList.color)
