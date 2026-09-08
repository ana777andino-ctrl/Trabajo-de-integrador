from funciones import(
    registrar_vaca,
    obtener_inventario,
    buscar_por_id,
    obtener_historial
)

while True:
    print("\n============== SISTEMA DE INVENTARIO DE LA APLICACIÓN BOXRUS=============")
    print("1. Registrar vaca")
    print("2. Listar vacas registradas")
    print("3. Buscar vaca por ID")
    print("4. Mostrar historial de vacas")
    print("5. Salir")
    print("\n=========================================================================")

    opcion =input("\nSeleccione una opción: ")

    if opcion == "1":
        try: 
            id =input("ID de Arete de la vaca: ").strip()
            nombre = input("Nombre de la vaca: ").strip()
            raza =input("Raza : ").strip()
            cédula = input("Cédula del dueño: ").strip()
            color = input("Color de la vaca: ").strip()
            peso = float(input("Peso de la vaca (Kg): ").strip())
            departamento = input("Departamento: ").strip()


            if id == "" or nombre == "" or raza == "": 
                print("Los datos de texto son obligatorios.") 
            elif peso < 0 : 
                print("El peso no puede ser negativo") 
            elif registrar_vaca(id, nombre, raza, cédula, color, peso, departamento): 
                print("Vaca registrada correctamente.") 
            else: 
                print("Ya existe una vaca con ese id.") 
        except ValueError:
                  print("Error de sistemas .") 
 
    elif opcion == "2": 
        vacas  = obtener_inventario() 
 
        if len(vacas) == 0: 
            print("No hay vacas registradas.") 
        else: 
            for vaca  in vacas: 
                print( 
                    vaca.id,
                    vaca.nombre,
                    vaca.raza, 
                    vaca.cédula,
                    vaca.color,
                    vaca.peso,
                    vaca.departamento
                ) 
 
    elif opcion == "3": 
        id = input("ID de arete de vaca a buscar: ").strip() 
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

