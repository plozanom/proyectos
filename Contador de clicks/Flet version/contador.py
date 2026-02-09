import flet as ft


def main(page: ft.Page):
    page.title = "Contador de clicks"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    entrada = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def click_negativo(e):
        if int(entrada.value) > 0:
            entrada.value = str(int(entrada.value) - 1)

    def click_positivo(e):
        entrada.value = str(int(entrada.value) + 1)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=click_negativo),
                entrada,
                ft.IconButton(ft.Icons.ADD, on_click=click_positivo),
            ],
        )
    )


ft.run(main)
