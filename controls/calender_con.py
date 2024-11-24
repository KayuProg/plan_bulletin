import flet as ft

class calender_contents():
    def __init__(self):
        super().__init__()
        
        ####################### main bar ########################
        self.title=ft.Text("Tosay's schedule", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_500,)#TODOディスプレイのサイズに合わせて文字の大きさも変わるようにしたいね．
        self.title_container=ft.Container(content=self.title,alignment=ft.alignment.center)#containerを使ってTitleを中央配置
        self.main_bar=ft.Row(controls=[self.title_container],expand=True)

            
            
            
            

        
        self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保
        
        
        ######################## incorporate ########################        
        self.contents=ft.Column(controls=[self.main_bar,
                                         ft.Divider(color="white",height=1.5,thickness=1.5),                                      
                                          self.space
                                        ],expand=True)




    
        self.title=ft.Text("alkfjalj", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_500,)#TODOディスプレイのサイズに合わせて文字の大きさも変わるようにしたいね．
        self.title_container=ft.Container(content=self.title,alignment=ft.alignment.center)#containerを使ってTitleを中央配置
        
        
        
        self.contents=ft.Column(controls=[self.title_container,
                                     ft.Divider(color="white",height=1.5,thickness=1.5),
                                    ],expand=True)#expandで横画面の大きさに合わせる,height,thicknessでdividerの幅設定．

















