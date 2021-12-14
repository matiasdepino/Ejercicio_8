import persistencia_json

lista = []
while True:
    marcadelcoche = input("Marca del coche: ")
    if marcadelcoche == "fin":
        break
    modelodelcoche = input("Modelo del oche: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    datos = {}
    datos["marcadelcoche"] = marcadelcoche
    datos["modelodelcoche"] = modelodelcoche
    datos["combustible"] = combustible
    datos["cilindrada"] = cilindrada
    lista.append(datos)
persistencia_json.store(lista, "coches.txt")
lista = []
lista = persistencia_json.retrieve("coches.txt")
print("Lista Coches:", "\n", lista)