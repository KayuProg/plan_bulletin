import flet as ft

class frame_class(ft.Row):
    def __init__(self,a):
        super().__init__()
        self.title=ft.Text(f"{a}")