# total de rutas
numero_rutas = int(input("Ingrese la cantidad de rutas: "))
lista_rutas = []

# guarda rutas y su contenidos
for indice in range(numero_rutas):
    entrada_ruta = input(f"Ingrese la ruta y contenido {indice + 1}: ").strip().split(' ', 1)
    lista_rutas.append(entrada_ruta)

# total de transiciones
numero_transiciones = int(input("Ingrese la cantidad de transiciones: "))

# procesar cada transición
for indice in range(numero_transiciones):
    transicion = input(f"Ingrese la transicion {indice + 1}: ").strip()
    partes_transicion = transicion.split('/')    
    encontrado = False    
    # busca coincidencias
    for ruta_definida, contenido_ruta in lista_rutas:
        partes_ruta_definida = ruta_definida.split('/')        
        # evalua longitud de partes
        if len(partes_ruta_definida) == len(partes_transicion):
            coincide = True
            texto_salida = contenido_ruta            
            # compara partes por su posición
            for posicion in range(len(partes_ruta_definida)):
                if partes_ruta_definida[posicion].startswith(':'):
                    # reemplaza variable
                    nombre_variable = partes_ruta_definida[posicion][1:]
                    valor_variable = partes_transicion[posicion]
                    texto_salida = texto_salida.replace('{' + nombre_variable + '}', valor_variable)
                elif partes_ruta_definida[posicion] != partes_transicion[posicion]:
                    # si no coinciden
                    coincide = False
                    break            
            if coincide:
                print(texto_salida)
                encontrado = True
                break                
    # error
    if not encontrado:
        print("404 Not Found")