from funciones import(
    registrar_vaca,
    obtener_inventario,
    buscar_por_id,
    obtener_historial
)

while True:
    print("\n============== SISTEMA DE INVENTARIO=============")
    print("1. Registrar vaca")
    print("2. Listar invetario")
    print("3. Buscar vaca por ID")
    print("4. Mostrar historial de vacas")
    print("5. Salir")

    opcion =input("Seleccione una opción: ")

    if opcion == "1":
        try: 
            id =input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria =input("Categoria: ").strip()
            cédula = input("Cédula: ").strip()
            color = input("Color: ").strip()
            peso = float(input("Peso: ").strip())
            departamento = input("Departamento:").strip()


            if id == "" or nombre == "" or categoria == "": 
                print("Los datos de texto son obligatorios.") 
            elif peso < 0 : 
                print("El peso no puede ser negativo") 
            elif registrar_vaca(id, nombre, categoria, cédula, color, peso, departamento): 
                print("Producto registrado correctamente.") 
            else: 
                print("Ya existe una vaca con ese id.") 
        except ValueError:
                  print("Error de sistemas .") 
 
    elif opcion == "2": 
        vacas  = obtener_inventario() 
 
        if len(vacas) == 0: 
            print("No hay productos registrados.") 
        else: 
            for vaca  in vacas: 
                print( 
                    vaca.id, 
                    vaca.nombre, 
                    vaca.categoria, 
                    vaca.cedula,
                    vaca.color,
                    vaca.peso,
                    vaca.departamento
                ) 
 
    elif opcion == "3": 
        id = input("id de arete de vaca a buscar").strip() 
        id = buscar_por_id(id) 
 
        if id == None: 
            print("vaca no encontrado.") 
        else: 
            print(id) 
 
    elif opcion == "5": 
        for movimiento in obtener_historial(): 
            print(movimiento) 
 
    elif opcion == "6": 
        print("Programa finalizado.") 
        break 
 
    else: 
        print("Seleccione una opción válida.") 

