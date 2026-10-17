import flet as ft


def main(page: ft.Page):
    page.title = "Producción de Ganado"
    page.padding = 20

    id_produccion = ft.TextField(
        label="ID de producción",
        width=400
    )

    id_vaca = ft.TextField(
        label="ID de la vaca",
        width=400
    )

    fecha = ft.TextField(
        label="Fecha",
        width=400
    )

    cantidad_leche = ft.TextField(
        label="Cantidad de leche (litros)",
        width=400
    )

    observaciones = ft.TextField(
        label="Observaciones",
        width=400
    )

    mensaje = ft.Text()

    def guardar(e):
        mensaje.value = "Producción registrada correctamente."
        mensaje.update()

    page.add(
        ft.Text(
            "REGISTRO DE PRODUCCIÓN",
            size=28,
            weight=ft.FontWeight.BOLD
        ),

        id_produccion,
        id_vaca,
        fecha,
        cantidad_leche,
        observaciones,

        ft.ElevatedButton(
            text="Guardar producción",
            on_click=guardar
        ),

        mensaje
    )


ft.app(target=main)