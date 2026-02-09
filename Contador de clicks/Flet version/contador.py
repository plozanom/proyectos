import flet as ft


def main(page: ft.Page):
    page.title = "Contador de clicks"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def click_negativo(e):
        input.value = str(int(input.value) - 1)

    def click_positivo(e):
        input.value = str(int(input.value) + 1)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=click_negativo),
                input,
                ft.IconButton(ft.Icons.ADD, on_click=click_positivo),
            ],
        )
    )


ft.run(main)
