from controls import calender_con
from controls import tasks_con
import flet as ft
import time
    
def main(page: ft.Page):
    #iPad用のwindowサイズにしておく．
    page.window.width=1024
    page.window.height=768
    page.horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    page.title="Plan Bulletin"
    
    
    calender=calender_con.calender_contents()
    tasks=tasks_con.tasks_contents(page)    
    
    app=ft.Row(controls=[
                        calender.contents,#tasks開発のために一度実行しない．
                        ft.VerticalDivider(color="white",width=1.5,thickness=1.5),#CalenderとTasksの区切り線
                        tasks.contents],
                expand=True,spacing=0)#expandで縦画面サイズに合わせる,spacing=0でdividerの区切り消す．
    

    page.add(app)

    while 1:
        calender.calender_update()#これを実行するとカレンダーの内容がupdateされる．
        # tasks.tasks_list_create()#これを実行するとtasksがupdateされる．
        page.update()
        time.sleep(1)




ft.app(main)
