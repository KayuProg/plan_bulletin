from controls import frame
import flet as ft


def main(page: ft.Page):
    page.title="Plan Bulletin"
    
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    calender_frame=frame.frame_class("thankyou")
    a_frame=frame.frame_class("fack")
    # page.add(calender_frame.title)
    # page.add(a_frame.title)
    
    titels=ft.Row(controls=[calender_frame.title,a_frame.title])
    page.add(titels)
    page.update()

ft.app(main)

