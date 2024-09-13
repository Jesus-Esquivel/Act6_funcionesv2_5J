print("Funciones Version 2")
print("Esquivel Adrian")
# zona de listas Tuplas , set y diccionarios
celulares=["Samsung A52","Huawei","iphone 12","Motorola","Nokia"]
carros=["Corvette","Mazda","Porsche","Mclaren","Nissan GT-R"]
jet={"Gulfstream","Bombardier Global 6000","Cessna Citation X+"}
print(jet)
print("Lista de Marcas de avion")
for marca in jet:
    print(marca)
#zona de tupla
def vermarca(carritos):
    for unamarca in carritos:
        print(unamarca)

#zona de Diccionarios
camionetas={
    "Marca":"BYD",
    "Modelos":"Shark",
    "year": 2024,
    "Valor": 899.980
}

# Zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
# Llamadas a funciones

print("Imprime celulares de una lista")
verlista(celulares)

print("Imprime una marca de carros")
vermarca(carros)

print(camionetas)
print("Camioneta")
for camionet in camionetas:
    print(camionetas[camionet])