import flet as ft


def main(page: ft.Page):
    page.title = "Mi primera aplicación con Flet"
    page.add(ft.Text("¡Mi primer proyecto!"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=30032)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
