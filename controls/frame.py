import flet as ft

class frame_class(ft.Row):
    def __init__(self):
        super().__init__()
        self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)

        self.col=ft.Column(controls=[self.space],expand=True)#expandで横画面の大きさに合わせる

