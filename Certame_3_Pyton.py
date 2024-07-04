import csv

# Lista para almacenar los pedidos
pedidos = []

# Función para registrar un pedido
def reg_pedido():
    print("\nRegistro de Pedido")
    print("------------------")
    cliente = input("Nombre del cliente: ")
    comuna = input("Comuna: ")
    
    # Validación de la comuna
    while comuna not in ["Concepcion", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]:
        print("Comuna inválida. Las comunas válidas son: Concepción, Chiguayante, Talcahuano, Hualpén, San Pedro.")
        comuna = input("Comuna: ")
        print (comuna)
    
    detalle_pedido = {
        'ID pedido':len(pedidos)+1,
        'Cliente': cliente,
        'Comuna': comuna,
        'Disp.6lts': 0,
        'Disp.10lts': 0,
        'Disp.20lts': 0
    }

    
    #dispensadores
    try:
        detalle_pedido['Disp.6lts'] = int(input("Ingrese dispensadores de 6 lts: "))
        detalle_pedido['Disp.10lts'] = int(input("Ingrese dispensadores de 10 lts: "))
        detalle_pedido['Disp.20lts'] = int(input("Ingrese dispensadores de 20 lts: "))
        
        if detalle_pedido['Disp.6lts'] + detalle_pedido['Disp.10lts'] + detalle_pedido['Disp.20lts'] <= 0:
            print("Debe ingresar por lo menos un dspensador.")
            return
        
        
        # Agregar el pedido a la lista de pedidos
        pedidos.append(detalle_pedido)
        print(f"El ID del pedido es: {detalle_pedido['ID pedido']}")
        
    except ValueError:
        print("Error: Debe ingresar valores numéricos para las cantidades de dispensadores.")

# lista pedidos
def listar_pedidos():
    if not pedidos:
        print("\nNo hay pedidos registrados.")
    else:
        print("\nListado de Pedidos")
        print("------------------")
        print(f"{'ID pedido':<10} {'Cliente':<20} {'Comuna':<15} {'Disp.6lts':<10} {'Disp.10lts':<10} {'Disp.20lts':<10}")
        for pedido in pedidos:
            print(f"{pedido['ID pedido']:<10} {pedido['Cliente']:<20} {pedido['Comuna']:<15} {pedido['Disp.6lts']:<10} {pedido['Disp.10lts']:<10} {pedido['Disp.20lts']:<10}")

#hoja de ruta
def imprimir_hoja_de_ruta():
    if not pedidos:
        print("\nNo se puede generar hoja de ruta sin pedidos.")
        return
    
    print("\nSectores disponibles: Concepción, Chiguayante, Talcahuano, Hualpén, San Pedro")
    sector = input("Seleccione un sector para generar la hoja de ruta: ")
    
    # Validación de sector
    while sector not in ["Concepcion", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]:
        print("Sector inválido. Por favor, seleccione un sector válido.")
        sector = input("Seleccione un sector para generar la hoja de ruta: ")
    
    # Filtrar pedidos por sector
    pedidos_sector = [pedido for pedido in pedidos if pedido['Comuna'] == sector]
    
    # Generar archivo CSV
    nombre_archivo = f"hoja_de_ruta_{sector}.csv"
    try:
        with open(nombre_archivo, mode='w', newline='') as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=['ID pedido', 'Cliente', 'Comuna', 'Disp.6lts', 'Disp.10lts', 'Disp.20lts'])
            escritor_csv.writeheader()
            for pedido in pedidos_sector:
                escritor_csv.writerow(pedido)
        
        print(f"\nHoja de ruta generada correctamente: {nombre_archivo}")
        print(f"\nDetalle de Archivo generado:")
        with open(nombre_archivo, mode='r', newline='') as archivo:
            for pedido in pedidos_sector:
                print (pedidos_sector)
        
    except IOError:
        print(f"Error al escribir el archivo: {nombre_archivo}")

# Buscar un pedido por ID
def buscar_pedido_por_id():
    if not pedidos:
        print("\nNo hay pedidos registrados.")
        return
    
    try:
        id_pedido = int(input("\nIngrese el ID del pedido a buscar: "))
        
        # Buscar el pedido por ID
        encontrado = False
        for pedido in pedidos:
            if pedido['ID pedido'] == id_pedido:
                encontrado = True
                print("\nDetalle del pedido encontrado:")
                print(f"ID pedido: {pedido['ID pedido']}")
                print(f"Cliente: {pedido['Cliente']}")
                print(f"Comuna: {pedido['Comuna']}")
                print(f"Disp.6lts: {pedido['Disp.6lts']}")
                print(f"Disp.10lts: {pedido['Disp.10lts']}")
                print(f"Disp.20lts: {pedido['Disp.20lts']}")
        
        if not encontrado:
            print(f"El ID {id_pedido} no existe")
    
    except ValueError:
        print("Error: Debe ingresar un valor numérico para el ID del pedido.")

# Función principal para ejecutar el programa
def main():
    while True:
        print("\nSistema de Gestión de Pedidos - CleanWasser")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Buscar un pedido por ID")
        print("5. Salir del programa")
        
        
        try:
            opcion = int(input("\nIngrese la opción deseada: "))
            
            if opcion == 1:
                reg_pedido()
            elif opcion == 2:
                listar_pedidos()
            elif opcion == 3:
                imprimir_hoja_de_ruta()
            elif opcion == 4:
                buscar_pedido_por_id()
            elif opcion == 5:
                print("\nSaliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción del 1 al 5.")
        
        except ValueError:
            print("Error: Debe ingresar un valor numérico para seleccionar una opción.")

if __name__ == "__main__":
    main()