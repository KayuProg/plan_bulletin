import flet as ft

class calender_contents():
    def __init__(self):
        super().__init__()
        
        # self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保


        self.main_bar=ft.Row(controls=[ft.Text("Today's schedule")
                                    ],expand=True)

        #ここのappendでcontrolsを追加してく感じで．
        # self.col.controls.append(ft.Placeholder(color=ft.colors.random_color(),expand=True))
        self.col.controls.append(self.main_bar)






















