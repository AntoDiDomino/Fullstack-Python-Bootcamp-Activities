magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pele", "Juanes"]

def imprimir_nombres(mago, cientifico, otro):
    print("\n Antes de modificar: \n")
    for mago in magos:
        print("-", mago)
    for cientifico in cientificos:
        print("-", cientifico)
    for otro in otros:
        print("-", otro)
    print("\nAhora son así: \n")
    hacer_grandioso()
    for cientifico in cientificos:
        print("-", cientifico)
    for otro in otros:
        print("-", otro)

def hacer_grandioso():
    for mago in magos:
        print("-", "El gran", mago)

hacer_grandioso()

imprimir_nombres(magos, cientificos, otros)
