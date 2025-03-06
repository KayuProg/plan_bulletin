from controls import calender_con
from controls import tasks_con
import asyncio
import flet as ft
import time

# async def calender_control_create(instance):
#     result_control=instance.calender_list_create()
#     return result_control

    
async def main(page: ft.Page):
    #iPad用のwindowサイズにしておく．
    page.window.width=1024
    page.window.height=768
    page.horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    page.title="Plan Bulletin"
    
    
    calender_instance=calender_con.calender_contents()#instance作成
    tasks_instance=tasks_con.tasks_contents(page)   
    
    controls_create = await asyncio.gather(
        calender_instance.calender_list_create(),
        tasks_instance.tasks_list_create(),        
    )
    
    if controls_create[0]==0 and controls_create[1]==0:
        print("Controls create successful")
    
    app=ft.Row(controls=[
                        calender_instance.contents,
                        # calender.contents,#tasks開発のために一度実行しない．
                        ft.VerticalDivider(color="white",width=1.5,thickness=1.5),#CalenderとTasksの区切り線
                        tasks_instance.contents],
                expand=True,spacing=0)#expandで縦画面サイズに合わせる,spacing=0でdividerの区切り消す．
    

    page.add(app)

    while 1:
        await asyncio.gather(
            calender_instance.calender_list_create(),
            tasks_instance.tasks_list_create(),  
        )
        page.update()
        time.sleep(4.5)


#非同期処理のためこっちを採用．
asyncio.run(ft.app(target=main))
# ft.app(main)
