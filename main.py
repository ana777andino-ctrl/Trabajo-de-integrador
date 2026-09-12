from funciones import registrar_vaca, obtener_inventario, buscar_por_id, obtener_historial, registrar_finca, obtener_fincas, registrar_vendedor, obtener_vendedores, registrar_remedio, obtener_remedios, registrar_comprador, obtener_compradores


def mostrar_lista(titulo, elementos):
    print(f"\n--- {titulo} ---")
    if not elementos:
        print("No hay registros.")
        return
    for elemento in elementos:
        print(elemento)


def registrar_vaca_menu():
    try:
        datos = [input("ID de arete: ").strip(), input("Nombre: ").strip(),
                 input("Raza: ").strip(), input("Cédula del dueño: ").strip(),
                 input("Color: ").strip(), float(input("Peso (kg): ").strip()),
                 input("Departamento: ").strip()]
        textos_obligatorios = datos[:5] + [datos[6]]
        if not all(textos_obligatorios):
            print("Los datos de texto son obligatorios.")
        elif datos[5] < 0:
            print("El peso no puede ser negativo.")
        elif registrar_vaca(*datos):
            print("Vaca registrada correctamente.")
        else:
            print("Ya existe una vaca con ese ID.")
    except ValueError:
        print("Los valores numéricos no son válidos.")


def registrar_finca_menu():
    try:
        datos = [input("Nombres del propietario: "), input("Apellidos: "),
                 input("Cédula: "), input("Celular: "), input("Nombre de la finca: "),
                 input("Nombre descriptivo: "), input("ID de finca: ")]
        print("Finca registrada correctamente." if registrar_finca(*datos)
              else "Ya existe una finca con ese ID.")
    except ValueError:
        print("Los valores numéricos no son válidos.")


def registrar_vendedor_menu():
    try:
        datos = [input("Nombre: "), input("Apellidos: "), input("Cédula: "),
                 input("Celular: "), input("ID de finca: "), input("ID de vaca: "),
                 input("Peso: "), input("Antecedentes: "),
                 input("¿Comprada? (s/n): ").lower() == "s",
                 input("¿Criollo? (s/n): ").lower() == "s", input("Ubicación: "),
                 input("Departamento: "), input("Precio de venta: ")]
        print("Vendedor registrado correctamente." if registrar_vendedor(*datos)
              else "Ya existe un vendedor con esa cédula.")
    except ValueError:
        print("Los valores numéricos no son válidos.")


def registrar_remedio_menu():
    try:
        datos = [input("Nombre: "), input("Descripción: "), input("Precio: "), input("Cantidad: ")]
        print("Remedio registrado correctamente." if registrar_remedio(*datos)
              else "Ya existe un remedio con ese ID.")
    except ValueError:
        print("Los valores numéricos no son válidos.")


def registrar_comprador_menu():
    try:
        datos = [input("Nombre: "), input("Apellidos: "), input("Cédula: "),
                 input("Celular: "), input("Departamento: "), input("Presupuesto: ")]
        print("Comprador registrado correctamente." if registrar_comprador(*datos)
              else "Ya existe un comprador con esa cédula.")
    except ValueError:
        print("Los valores numéricos no son válidos.")


while True:
    print("\n===== SISTEMA DE LA APLICACIÓN DE LA EMPRESA BOXRUS=====")
    print("1. Registrar vaca    2. Listar vacas    3. Buscar vaca")
    print("4. Historial vacas   5. Registrar finca 6. Listar fincas")
    print("7. Registrar vendedor 8. Listar vendedores")
    print("9. Registrar remedio 10. Listar remedios")
    print("11. Registrar comprador 12. Listar compradores")
    print("0. Salir")
    opcion = input("\nSeleccione una opción: ").strip()
    try:
        if opcion == "1": registrar_vaca_menu()
        elif opcion == "2": mostrar_lista("Vacas", obtener_inventario())
        elif opcion == "3":
            encontrado = buscar_por_id(input("ID de arete: "))
            print(encontrado if encontrado else "Vaca no encontrada.")
        elif opcion == "4": mostrar_lista("Historial", obtener_historial())
        elif opcion == "5": registrar_finca_menu()
        elif opcion == "6": mostrar_lista("Fincas", obtener_fincas())
        elif opcion == "7": registrar_vendedor_menu()
        elif opcion == "8": mostrar_lista("Vendedores", obtener_vendedores())
        elif opcion == "9": registrar_remedio_menu()
        elif opcion == "10": mostrar_lista("Remedios", obtener_remedios())
        elif opcion == "11": registrar_comprador_menu()
        elif opcion == "12": mostrar_lista("Compradores", obtener_compradores())
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else: print("Seleccione una opción válida.")
    except ValueError:
        print("El dato numérico no es válido.")

