# Definición con con for y cobdicionales para buscar mas rapido.

# Definición
def fincas_grandes (lista_finas):
        print("                    Lista de Fincas Mayores de 20 Hectareas")
        print("                   -------------------------------------------")
        print()

#Ponemos un contador para saber cuantos existen
        contador=0
        for Dato in lista_finas:
             if Dato["Hectareas"] > 20 :
                 print(f" Nombre : {Dato["Nombre_finca"]} | Ubicación :{Dato["Ubicación"]} | Hectareas :{Dato["Hectareas"]}" )
                 contador +=1
                 print("------------------------------------------------------------------")
        print()
        print()
        print(f"La cantidad de fincas mayores a 20 son : | {contador} en total |\n  ")

# Ponemos la lista
lista=[{"Nombre_finca":"La Libertad", "Ubicación":"Santa Elena", "Hectareas": 16.8},
{"Nombre_finca":"Macas", "Ubicación":"La Maná", "Hectareas": 20.5},
{"Nombre_finca":"Arena", "Ubicación":"Guayas", "Hectareas": 35.3},
{"Nombre_finca":"El Potral", "Ubicación":"Manabí", "Hectareas": 50.7},
{"Nombre_finca":"El Arcos", "Ubicación":"Manta", "Hectareas": 23.1},
{"Nombre_finca":" Rea", "Ubicación":"Esmeraldas", "Hectareas": 38.9},
{"Nombre_finca":" Sanchez ", "Ubicación":"Los Rios", "Hectareas": 18.5},
{"Nombre_finca":"El Martillo ", "Ubicación":"Milagro", "Hectareas": 90.3},
{"Nombre_finca":"La pasta ", "Ubicación":"Sapotal", "Hectareas": 9.2},
{"Nombre_finca":"Estrias ", "Ubicación":"Maisal", "Hectareas": 87.8},
{"Nombre_finca":" El Canguro ", "Ubicación":"Cuenca", "Hectareas": 64.5},
{"Nombre_finca":" La Caprichoza ", "Ubicación":"Ambato", "Hectareas": 14.6} ]

# Llamamos a la función
fincas_grandes(lista)