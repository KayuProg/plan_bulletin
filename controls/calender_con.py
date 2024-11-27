import flet as ft

class calender_contents():
    def __init__(self):
        super().__init__()
        
        ####################### main bar ########################
        
        #TODOディスプレイのサイズに合わせて文字の大きさも変わるようにしたいね．
        self.title=ft.Text("Tosay's schedule", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_500,)
        self.title_container=ft.Container(content=self.title,alignment=ft.alignment.center)#containerを使ってTitleを中央配置
        self.back_date=ft.IconButton(icon=ft.icons.ARROW_CIRCLE_LEFT, on_click=self.back_date_func)
        self.forward_date=ft.IconButton(icon=ft.icons.ARROW_CIRCLE_RIGHT, on_click=self.forward_date_func)
        self.main_bar=ft.Row(controls=[self.back_date,self.title_container,self.forward_date],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

        
        self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保
        
        
        ######################## incorporate ########################        
        self.contents=ft.Column(controls=[self.main_bar,
                                         ft.Divider(color="white",height=1.5,thickness=1.5),                                      
                                          self.space
                                        ],expand=True)

    
    def back_date_func(self,e):#TODO関数の作成
        pass
    
    def forward_date_func(self,e):#TODO関数の作成
        pass
    
    
    def button_clicked(self,e):
        print(0)




