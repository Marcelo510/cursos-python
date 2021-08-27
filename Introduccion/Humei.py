

base = {
    1: {"nombre":"Fernanda",
        "apellido":"Fernandez",
        "dni":333333331},
    2: {"nombre":"Gonzalo",
        "apellido":"Gonzalez",
        "dni":333333332},
    3: {"nombre":"Rodrigo",
        "apellido":"Rodriguez",
        "dni":333333333}
    }

dnis = [333333331, 333333336, 333333339, 333333332, None, 333333333]

n_encontrados = 0

for dni in dnis: # itero por todos los dnis

    if type(dni) == int: # si el tipo es entero
        dni_encontrado = False # inicializo una variable con valor False, ya van a ver para qué :-)
        
        # Ahora viene la parte complicada, ¿cómo sé si ese dni ya está en mi base?
        # 1- Recordemos que base es un diccionario y como tal tiene el método items(), pruébenlo afuera de esta celda
        # me devuelve una tupla, con la llave en el primer elemento y el valor en el segundo
        
        # itero por todos los elementos
        for i in base.items(): 
            valor = i[1] # guardo el valor en una variable
            if dni == valor["dni"]: # si el dni es el mismo que estoy buscando...
                dni_encontrado = True
                nombre_completo = valor["nombre"] + " " + valor["apellido"]
                n_encontrados += 1 # esto equivale a encontrados = encontrados + 1, agrega uno
                break # freno la búsqueda, ésto evita que siga buscando

        if dni_encontrado: # entra acá si es True
            print(f"{nombre_completo.title()} ingreso a nuestra web")

        elif not dni_encontrado: # noten el not
            print(f'El dni {dni} no se encuentra en la base...')
            continue # sigo con la búsqueda, NO paso a la siguiente línea
            
        print(f"Hasta el momento se encontraron {n_encontrados} casos")
    
    else:
        pass # si dni no es un entero entonces no hacemos nada, suponemos que hubo algún tipo de error

registro = ('Argentina', 112000, 'Bariloche')

registro[0] 

pais, poblacion, ciudad = registro

print("País:", pais)
print("Población:", poblacion)
print("Ciudad:", ciudad)

registros = [registro, ('Brasil', 477000, 'Florianópolis')]
print(registros[1])

# Una lista sí se puede modificar
lista = [1, 2, 3]

lista[0] = 4

lista

print(str(type(lista)) + "->" + str(type(registros)) + '->' + str(type(registro)))
