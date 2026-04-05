# datos iniciales
entrada_principal = input("Ingrese N M S: ").strip().split()
numero_socios = int(entrada_principal[0])
numero_terminales = int(entrada_principal[1])
numero_transacciones = int(entrada_principal[2])
mapa_terminal_socio = {}

# terminales
for indice in range(numero_terminales):
    entrada_terminal = input(f"Socio y terminal {indice + 1}: ").strip().split()
    id_socio = int(entrada_terminal[0])
    id_terminal = int(entrada_terminal[1])
    mapa_terminal_socio[id_terminal] = id_socio

# compras por socio
compras_por_socio = {}
for socio in range(1, numero_socios+1):
    compras_por_socio[socio] = {}

# transacciones
for indice in range(numero_transacciones):
    entrada_transaccion = input(f"Cliente y terminal transaccion {indice + 1}: ").strip().split()
    id_cliente = int(entrada_transaccion[0])
    id_terminal = int(entrada_transaccion[1])
    # verifica si existe
    if id_terminal in mapa_terminal_socio:
        id_socio = mapa_terminal_socio[id_terminal]        
        # suma la compra
        if id_cliente not in compras_por_socio[id_socio]:
            compras_por_socio[id_socio][id_cliente] = 0
        compras_por_socio[id_socio][id_cliente] += 1

# por socio
print("\nResultados:")
for id_socio in range(1, numero_socios + 1):
    clientes_del_socio = compras_por_socio[id_socio]    
    # verifica si hay compras
    if not clientes_del_socio:
        print(f"{id_socio} -1")
    else:
        cliente_fiel = -1
        maximo_compras = -1        
        # busca al mas fiel
        for id_cliente, cantidad in clientes_del_socio.items():
            # compara compras e id
            if cantidad > maximo_compras:
                maximo_compras = cantidad
                cliente_fiel = id_cliente
            elif cantidad == maximo_compras and id_cliente < cliente_fiel:
                cliente_fiel = id_cliente                
        # imprime el mejor
        print(f"{id_socio} {cliente_fiel}")