from controls import frame
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    page.title="Plan Bulletin"
    
    calender_frame=frame.frame_class()
    tasks_frame=frame.frame_class()
    
    titels=ft.Row(controls=[calender_frame.col,tasks_frame.col],expand=True)#expandで縦画面サイズに合わせる
    

    page.add(titels)
    page.update()

ft.app(main)
