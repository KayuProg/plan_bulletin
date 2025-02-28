import flet as ft

#実行場所によるかも
import get_info.calender as calender

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


        
        ######################## incorporate ########################     
        


        self.plans=[]#ここに，[時間，内容，説明]のlistを入れていく
                
                
        self.list=self.calender_list_create()
        
        self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保

        #このself.contentsをmain.pyで呼び出して使用する．
        self.contents=ft.Column(controls=[self.main_bar,
                                         ft.Divider(color="white",height=1.5,thickness=1.5),                                      
                                          self.space,self.list
                                        ],expand=True)

    
    def back_date_func(self,e):#TODO関数の作成
        pass
    
    def forward_date_func(self,e):#TODO関数の作成
        pass

    
    def calender_list_create(self):#list_contents_createをforで繰り返してself.contentsのcolumnに入れるリスト作成
        plan_count=0#その日の予定の数をカウントする．
         
        result=calender.main()
               
        time=ft.Text("11:22", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_100,)
        plan_con=ft.Text("Tosay", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_100,)
        description=ft.Text("Tosay's scul", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,weight=ft.FontWeight.W_100,)
        
        list_parent=ft.Row(controls=[time,plan_con,description],expand=True,spacing=0)#Columnに入れる
        
        return list_parent
        
class list_contents_create():
    def __init__(self):
        super().__init__()
        
        # self.calender_lsit=
        print(10)
        