import flet as ft
import get_info.tasks as task
import datetime
import time
#実行場所によるので注意
import get_info.tasks as tasks

class tasks_contents():
    def __init__(self,page):
        super().__init__()
  ####################### main bar ########################
        
        #TODOディスプレイのサイズに合わせて文字の大きさも変わるようにしたいね．
        # self.title=ft.Stack(ft.Text(spans=[ft.TextSpan("Tosay's schedule", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,weight=ft.FontWeight.W_500,color="black"))],
        #                     ft.Text("Tosay's schedule", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,weight=ft.FontWeight.W_800,color="white"),)
        
        self.page=page
        self.title_text_black = ft.Text(
            spans=[
                ft.TextSpan(
                    "Remaining Tasks",
                    ft.TextStyle(
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            color="black",
                            stroke_width=3,
                            stroke_join=ft.StrokeJoin.ROUND,
                            style=ft.PaintingStyle.STROKE,
                        ),
                    ),
                ),
            ],
        )
        self.title_text_white = ft.Text(
            spans=[
                ft.TextSpan(
                    "Remaining Tasks",
                    ft.TextStyle(
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                ),
            ],
        )
        self.title = ft.Stack([self.title_text_black, self.title_text_white])
        
        self.title_container=ft.Container(content=self.title,alignment=ft.alignment.center)#containerを使ってTitleを中央配置   
        decolate=ft.Icon(name=ft.icons.TASK_ALT,size=40,color="#0000cd")
        self.main_bar=ft.Container(content=ft.Row(controls=[decolate,self.title_container,decolate],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                   bgcolor="blue",
                                   height=80,
                                )
        
        
        
        ######################## incorporate ########################     
        

        self.display_flag=1#1の時にはremainが表示されている．0のときにはcompletedが表示されている．
        self.remain=ft.Column(controls=[],spacing=5,expand=True)
        self.completed=ft.Column(controls=[],spacing=5,expand=True)
        
        self.tasks_list=ft.Column(controls=[self.remain],expand=True)#ここにのlistを入れていく


        #self.plansにlistを作成する関数の実行
        self.tasks_list_create()
        
        
        self.refresh=ft.Container(content=ft.TextButton(
                                                        content=ft.Icon(name=ft.icons.REFRESH, color="#00bfff",size=50),
                                                        # alignment=ft.MainAxisAlignment.SPACE_AROUND,)
                                                        on_click=self.refresh_tasks),
                                # bgcolor="brown",
                                margin=ft.margin.only(0,0,0,10),
                                alignment=ft.alignment.bottom_right,
                                )

        # self.refresh=ft.Container(content=ft.ElevatedButton(text="Refresh",on_click=self.refresh_tasks,
        #                                                           style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)),
        #                                                           bgcolor="#65656565"),
        #                                 margin=ft.margin.only(0,0,0,10),
        #                                 alignment=ft.alignment.top_right,
        #                                 )
        self.change_button=ft.Container(content=ft.ElevatedButton(text="Change Display",on_click=self.change_display,
                                                                  style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)),
                                                                  bgcolor="#65656565"),
                                        margin=ft.margin.only(0,0,0,15),
                                        alignment=ft.alignment.top_right,
                                        )
        
        # self.space= ft.Placeholder(color=ft.colors.random_color(),expand=True)#一時的な場所確保

        #このself.contentsをmain.pyで呼び出して使用する．
        self.contents=ft.Column(controls=[self.main_bar,
                                          ft.Container(content=ft.Divider(color="white",height=1.5,thickness=1.5),margin=ft.margin.only(0,0,0,20),),
                                          self.change_button,
                                          self.tasks_list,
                                          self.refresh
                                        ],expand=True,spacing=0)

    def change_display(self,e):        
        self.tasks_list.controls.clear()
        if self.display_flag==1:#消化済みタスク
            self.tasks_list.controls.append(self.completed)
            self.display_flag=0
            self.title_text_black.spans[0].text = "Completed Tasks"
            self.title_text_white.spans[0].text = "Completed Tasks"
            self.main_bar.bgcolor = "red"

        elif self.display_flag==0:#未消化タスク
            self.tasks_list.controls.append(self.remain)
            self.display_flag=1
            self.title_text_black.spans[0].text = "Remaining Tasks"
            self.title_text_white.spans[0].text = "Remaining Tasks"
            self.main_bar.bgcolor = "blue"

        self.page.update()

    
    def tasks_list_create(self):
        
        self.remain.controls.clear()
        self.completed.controls.clear()


        #APIからtasksを取得する．
        events=tasks.main()
        list_con=[]      
        
        for event in events:
            # print(event)
            
            title=event["title"]
            note=event["note"]
            status=event["status"]#needsAction or cpmleted
            due_check=event["due_check"]#not_expired or expired
            
            task_id=event["task_id"]
           
            due=event["due"] 
            due_date=datetime.datetime.fromisoformat(due).strftime("%m-%d")
            today=datetime.datetime.today().strftime("%m-%d")
            
            # print(due_date)
            
            #########################################################
            #control作成
            #########################################################
            due_date_control=ft.Container(content=ft.Text(due_date,size=25,weight=ft.FontWeight.W_500,),
                              alignment=ft.alignment.center,
                              width=100,
                            #   height=30,
                              margin= ft.margin.only(0,0,5,0),padding=0,
                              border_radius=0,
                              )
            
            if due_check=="expired":#期限切れ
                title_control=ft.Container(content=ft.Text(title,size=25,weight=ft.FontWeight.W_500,color="red"),
                                alignment=ft.alignment.center_left,
                                width=330,
                                # height=50,
                            #   margin= ft.margin.symmetric(vertical=10),padding=0,
                                border_radius=0,
                                )
            elif due_check=="not_expired":
                title_control=ft.Container(content=ft.Text(title,size=25,weight=ft.FontWeight.W_500,),
                                alignment=ft.alignment.center_left,
                                width=330,
                                # height=50,
                            #   margin= ft.margin.symmetric(vertical=10),padding=0,
                            #   border_radius=0,
                                )
            
            note_control=ft.Container(content=ft.Text(note,size=18,weight=ft.FontWeight.W_400,),
                            # bgcolor="grey",
                            alignment=ft.alignment.center_left,
                            width=320,
                        #   height=50,
                            margin= ft.margin.only(20,0,0,0),padding=0,
                        #   border_radius=0,
                            )
            # print(note)
            #add note
            title_display=title_control

            if note==None:
                title_display=title_control
            else :
                title_display=ft.Column(controls=[title_control,note_control],spacing=0)
            
            
            if status=="needsAction":
                btn= ft.Switch(value=False,on_change=lambda e,tid=task_id, ts=status:self.task_complete(tid, ts,e.control.value))
            elif status=="completed":
                btn= ft.Switch(value=True,on_change=lambda e,tid=task_id, ts=status:self.task_complete(tid, ts,e.control.value))
                
            
            
        #     if event["desc"]==None:#descriptionに何も記述ない場合はcolumnを作成しない．
        #         plan_column=plan_con
        #     else:
        #         plan_column=ft.Column(controls=[plan_con,description],expand=True,spacing=0)

            list_con=ft.Container(content=ft.Row(controls=[due_date_control,title_display,btn],spacing=0),margin=ft.margin.only(0,0,0,0))

            if status=="needsAction":
                self.remain.controls.append(list_con)

            elif status=="completed":
                self.completed.controls.append(list_con)
                
        return 0
    
    def task_complete(self,tid,ts,val):
        tasks.change_status(tid, ts,val)
        #ここにtasksの表示をupdateする関数の実行を書く．
        time.sleep(2)#スライドスイッチの変化がGoogle Tasksに反映されるまで待つ
        self.tasks_list_create()
        self.page.update()
        
        return 0
        
        
    def refresh_tasks(self,e):
        print("refreshing")
        self.tasks_list_create()
        self.page.update()
        return 0
        