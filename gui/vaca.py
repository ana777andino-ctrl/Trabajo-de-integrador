import flet as ft 
from funciones import obtener_inventario, registrar_vaca
 
def vista_vacas(page: ft.Page): 
    txt_id = ft.TextField(label="ID de Arete", expand=1)
    txt_nombre = ft.TextField(label="Nombre", expand=2)
    txt_raza = ft.TextField(label="Raza", expand=1)
    txt_cedula = ft.TextField(label="Cédula del Dueño", expand=2)
    txt_color = ft.TextField(label="Color", expand=1)
    txt_peso = ft.TextField(
      label="Peso (kg)", keyboard_type=ft.KeyboardType.NUMBER, expand=1
 
     
    ) 
    txt_depto = ft.TextField(label="Departamento", expand=1)

    tabla = ft.DataTable(
      columns=[
          ft.DataColumn(ft.Text("ID")),
          ft.DataColumn(ft.Text("Nombre")),
          ft.DataColumn(ft.Text("Raza")),
          ft.DataColumn(ft.Text("Dueño (Cédula)")),
          ft.DataColumn(ft.Text("Peso")),
          
      ],
      rows=[],
  )
    def refrescar():
    tabla.rows.clear()
    for v in obtener_inventario():
      tabla.rows.append(
          ft.DataRow(
              cells=[
                  ft.DataCell(ft.Text(str(v.id))),
                  ft.DataCell(ft.Text(v.nombre)),
                  ft.DataCell(ft.Text(v.raza)),
                  ft.DataCell(ft.Text(str(v.cédula))),
                  ft.DataCell(ft.Text(str(v.peso))),
                  ft.DataCell(ft.Text(v.departamento)),
              ]
          )
      )
 page.update()

  def guardar(e, txt_id, txt_raza, txt_color, txt_peso):
    class txt_nombre:
      ...

    class txt_cedula:
      ...

    class txt_depto:
      ...

    exito = registrar_vaca(
        txt_id.value,
        txt_nombre.value,
        txt_raza.value,
        txt_cedula.value,
        txt_color.value,
        txt_peso.value,
        
    )
    if exito:
      txt_id.value = ""
      txt_nombre.value = ""
      txt_raza.value = ""
      txt_cedula.value = ""
      txt_color.value = ""
      txt_peso.value = ""
      txt_depto.value = ""
      def refrescar():
        ...

      refrescar()
      class page:
        ...

      page.snack_bar = ft.SnackBar(ft.Text("¡Vaca registrada con éxito!"))
    else:
      page.snack_bar = ft.SnackBar(
          ft.Text("Error: Ya existe una vaca con ese ID o datos inválidos.")
      )
    page.snack_bar.open = True
    page.update()

  def refrescar():
    ...

  refrescar()

  class txt_id:
    ...

  class txt_nombre:
    ...

  class txt_raza:
    ...

  class txt_cedula:
    ...

  class txt_color:
    ...

  class txt_peso:
    ...

  return ft.Column(
      [
          ft.Text(
              "Gestión de Vacas",
              size=22,
              weight=ft.FontWeight.BOLD,
              color=ft.Colors.GREEN_800,
          ),
          ft.Row([txt_id, txt_nombre, txt_raza]),
          ft.Row([txt_cedula, txt_color, txt_peso, txt_peso]),
          ft.ElevatedButton(
              "Registrar Vaca",
              icon=ft.Icons.SAVE,
              on_click=guardar,
              bgcolor=ft.Colors.GREEN_700,
              color=ft.Colors.WHITE,
          ),
          ft.Divider(),
          ft.Text("Inventario de Vacas", weight=ft.FontWeight.BOLD),
          ft.Column([tabla], scroll=ft.ScrollMode.AUTO, expand=True),
      ],
      expand=True,
  )
    