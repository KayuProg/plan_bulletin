from controls import calender_con
from controls import tasks_con
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    page.title="Plan Bulletin"
    
    calender=calender_con.calender_contents()
    tasks=tasks_con.tasks_contents()    
    
    app=ft.Row(controls=[calender.contents,
                        ft.VerticalDivider(color="white",width=1.5,thickness=1.5),#CalenderとTasksの区切り線
                        tasks.contents]
                  ,expand=True,spacing=0)#expandで縦画面サイズに合わせる,spacing=0でdividerの区切り消す．
    

    page.add(app)
    page.update()

ft.app(main)
