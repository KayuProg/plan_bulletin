import flet as ft
import datetime

#実行場所によるので注意
import get_info.calender as calender

class calender_contents():
    def __init__(self):
        super().__init__()
        
        ####################### main bar ########################
        
        #TODOディスプレイのサイズに合わせて文字の大きさも変わるようにしたいね．
        self.title=ft.Text("Tosay's schedule", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,weight=ft.FontWeight.W_500,)
        self.title_container=ft.Container(content=self.title,alignment=ft.alignment.center)#containerを使ってTitleを中央配置
        self.back_date=ft.IconButton(icon=ft.icons.ARROW_CIRCLE_LEFT, on_click=self.back_date_func)
        self.forward_date=ft.IconButton(icon=ft.icons.ARROW_CIRCLE_RIGHT, on_click=self.forward_date_func)
        self.main_bar=ft.Row(controls=[self.back_date,self.title_container,self.forward_date],alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        
        ######################## incorporate ########################     
        

        self.plans=ft.Column(controls=[],expand=True)#ここに，[時間，内容，説明]のlistを入れていく

        #self.plansにlistを作成する関数の実行
        self.calender_list_create()
        
        self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保

        #このself.contentsをmain.pyで呼び出して使用する．
        self.contents=ft.Column(controls=[self.main_bar,
                                          ft.Divider(color="white",height=1.5,thickness=1.5),                                      
                                          self.plans
                                        ],expand=True)

    
    def back_date_func(self,e):#TODO関数の作成
        pass
    
    def forward_date_func(self,e):#TODO関数の作成
        pass

    
    def calender_list_create(self):#list_contents_createをforで繰り返してself.contentsのcolumnに入れるリスト作成
        #APIより今日の予定の情報を拾ってくる．ファイルはcalender.py
        events=calender.main()
        list_con=[]
        for event in events:
            event_time=datetime.datetime.fromisoformat(event["date"]).strftime("%H:%M")
            if event_time=="00:00":
                event_time="All day"

            bg_color=event["color"]
            
            time=ft.Container(content=ft.Text(event_time,size=25,weight=ft.FontWeight.W_500,),
                              alignment=ft.alignment.center,
                              width=100,height=50,
                              margin= ft.margin.symmetric(vertical=10),padding=0,
                              border_radius=0,
                              )
            plan_con=ft.Text(event["summary"],size=30,weight=ft.FontWeight.W_100,bgcolor=bg_color,color="black",expand=True)
            description=ft.Text(event["desc"],size=10,weight=ft.FontWeight.W_100,bgcolor=bg_color,color="black",expand=True)
            
            plan_column=ft.Column(controls=[plan_con,description],expand=True,spacing=0)
            #TODO ここでColmnでdescriptionを入れるかどうかはdescriptionに記述があるかどうかで分岐させる．
            list_con=ft.Row(controls=[time,plan_column],spacing=10)

            self.plans.controls.append(list_con)
        return 0
        