from entidades import vaca, finca, vendedor, Remedio, comprador
from Datos import inventario, vacas_por_aretes, historial_movimiento, lista_finca, lista_vendedor, lista_remedio, lista_comprador


def _ya_existe(container, campo, valor):
    if isinstance(container, dict):
        return valor in container

    for item in container:
        if hasattr(item, campo) and getattr(item, campo) == valor:
            return True
    return False


def _guardar_entidad(container, entidad, clave, valor):
    if isinstance(container, dict):
        container[valor] = entidad
    else:
        container.append(entidad)
    return True


def registrar_vaca(id, nombre, raza, cédula, color, peso, departamento):
    id_entero = int(id)

    if _ya_existe(vacas_por_aretes, "id", id_entero):
        return False

    nueva_vaca = vaca(
        id=id_entero,
        nombre=nombre,
        raza=raza,
        cédula=cédula,
        color=color,
        peso=float(peso),
        departamento=departamento,
    )

    inventario.append(nueva_vaca)
    vacas_por_aretes[id_entero] = nueva_vaca

    historial_movimiento.append({
        "ID de arete": id_entero,
        "nombre": nombre,
        "raza": raza,
        "departamento": departamento,
    })

    return True


def obtener_inventario():
    return inventario


def buscar_por_id(id):
    return vacas_por_aretes.get(int(id))


def obtener_historial():
    return historial_movimiento


# Función para registrar una finca

def registrar_finca(nombres, apellidos, cédula, célular, nombre_finca, nombre_de_finca, ID_de_finca):
    id_finca = int(ID_de_finca)

    if _ya_existe(lista_finca, "ID_de_finca", id_finca):
        return False

    nueva_finca = finca(
        nombres=nombres,
        apellidos=apellidos,
        cédula=cédula,
        célular=int(célular),
        nombre_finca=nombre_finca,
        nombre_de_finca=nombre_de_finca,
        ID_de_finca=id_finca,
    )

    _guardar_entidad(lista_finca, nueva_finca, "ID_de_finca", id_finca)
    return True


def obtener_fincas():
    return lista_finca


def obtener_historial_finca():
    return lista_finca


def buscar_finca_por_id(id_finca):
    id_finca = int(id_finca)
    return next((item for item in lista_finca if item.ID_de_finca == id_finca), None)

# Registrar vendedor

def registrar_vendedor(nombre, apellidos, cédula, célular, ID_de_finca, ID_de_vaca, peso, antecedentes, comprada, criollo, ubicación, departamento, precio_de_venta):
    cédula = int(cédula)

    if _ya_existe(lista_vendedor, "cédula", cédula):
        return False

    nuevo_vendedor = vendedor(
        nombre=nombre,
        apellidos=apellidos,
        cédula=cédula,
        célular=int(célular),
        ID_de_finca=int(ID_de_finca),
        ID_de_vaca=int(ID_de_vaca),
        peso=float(peso),
        antecedentes=antecedentes,
        comprada=comprada,
        criollo=criollo,
        ubicación=ubicación,
        departamento=departamento,
        precio_de_venta=float(precio_de_venta),
    )

    _guardar_entidad(lista_vendedor, nuevo_vendedor, "cédula", cédula)
    return True


def obtener_vendedores():
    return lista_vendedor


def buscar_vendedor_por_cedula(cédula):
    cédula = int(cédula)
    return next((item for item in lista_vendedor if item.cédula == cédula), None)


# Registrar remedio

def registrar_remedio(nombre, descripcion, precio, cantidad, id_remedio=None):
    if id_remedio is None:
        ids = [item.id_remedio for item in lista_remedio if item.id_remedio is not None]
        id_remedio = max(ids, default=0) + 1
    else:
        id_remedio = int(id_remedio)

    if id_remedio is not None and _ya_existe(lista_remedio, "id_remedio", id_remedio):
        return False

    nuevo_remedio = Remedio(
        nombre=nombre,
        descripcion=descripcion,
        precio=float(precio),
        cantidad=int(cantidad),
        id_remedio=id_remedio,
    )

    if id_remedio is not None:
        _guardar_entidad(lista_remedio, nuevo_remedio, "id_remedio", id_remedio)
    else:
        lista_remedio.append(nuevo_remedio)
    return True


def obtener_remedios():
    return lista_remedio


def buscar_remedio_por_id(id_remedio):
    id_remedio = int(id_remedio)
    return next((item for item in lista_remedio if item.id_remedio == id_remedio), None)


# Registrar comprador

def registrar_comprador(nombre, apellidos, cédula, célular, departamento, presupuesto):
    cédula = int(cédula)

    if _ya_existe(lista_comprador, "cédula", cédula):
        return False

    nuevo_comprador = comprador(
        nombre=nombre,
        apellidos=apellidos,
        cédula=cédula,
        célular=int(célular),
        departamento=departamento,
        presupuesto=float(presupuesto),
    )

    _guardar_entidad(lista_comprador, nuevo_comprador, "cédula", cédula)
    return True


def obtener_compradores():
    return lista_comprador


def buscar_comprador_por_cedula(cédula):
    cédula = int(cédula)
    return next((item for item in lista_comprador if item.cédula == cédula), None)

