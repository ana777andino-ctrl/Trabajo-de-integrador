from entidades import vaca
from Datos import inventario, vacas_por_aretes, historial_movimiento


def registrar_vaca(id, nombre, raza, cédula, color, peso, departamento ):

    id_entero =int(id)

    if id_entero in vacas_por_aretes:
        return False

    nuevo = vaca(
        id=id_entero,
        nombre= nombre,
        raza= raza,
        cédula= cédula,
        color= color,
        peso= float(peso),
        departamento=departamento 

)

    inventario.append(nuevo)
    vacas_por_aretes[id_entero] = nuevo

    historial_movimiento.append({
        "ID de arete": id,
        "nombre": nombre,
        "raza":raza,
        "departamento": departamento
})

    return True

def obtener_inventario():
    return inventario

def buscar_por_id(id):
    return vacas_por_aretes.get(int(id))


def obtener_historial(): 
    return historial_movimiento