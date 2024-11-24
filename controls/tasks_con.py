import flet as ft

class tasks_contents():
    def __init__(self):
        super().__init__()
        self.contents=ft.Row(controls=[ft.Text("Current Tasks")
                                    ],expand=True)

