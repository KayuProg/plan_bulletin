from controls import frame
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    page.title="Plan Bulletin"
    
    calender_frame=frame.frame_class("Calender")
    tasks_frame=frame.frame_class("Tasks")
    
    app=ft.Row(controls=[calender_frame.col,
                            ft.VerticalDivider(color="white",width=1.5,thickness=1.5),#CalenderとTasksの区切り線
                            tasks_frame.col]
                  ,expand=True,spacing=0)#expandで縦画面サイズに合わせる,spacing=0でdividerの区切り消す．
    

    page.add(app)
    page.update()

ft.app(main)
