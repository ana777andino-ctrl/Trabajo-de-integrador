from entidades import vaca
from datos import inventario, vacas_por_aretes, historial_movimientos


def registrar_vaca(id, nombre, categoria, cédula, color, peso, departamento ):

    id_entero =int(id)

    if id_entero in vacas_por_aretes:
        return False

    nuevo = vaca(
        id=id_entero,
        nombre= nombre,
        categoria= categoria,
        cédula= cédula,
        color= color,
        peso= float(peso),
        departamento=departamento 

)

    inventario.append(nuevo)
    vacas_por_aretes[id_entero] = nuevo

    historial_movimientos.append({
        "tipo": "registro",
        "nombre": nombre,
        "departamento": departamento
})

    return True

def obtener_inventario():
    return inventario

def buscar_por_id(id):
    return buscar_por_id.get(int(id))


def obtener_historial(): 
    return historial_movimientos