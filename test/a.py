import flet as ft

te="kdkdk"
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""+"あ"
        global te
        te=te+"3939"
        a.value=te
        print(te)
        page.update()

    new_task = ft.TextField(hint_text="What's needs to be done?")
    a=ft.Text(te,size=25,weight=ft.FontWeight.W_500,)
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
    page.add(a)
ft.app(main)

# import flet as ft

# te = "kdkdk"  # グローバルな変数

# def main(page: ft.Page):
#     def add_clicked(e):
#         # チェックボックスを追加
#         page.add(ft.Checkbox(label=new_task.value))
        
#         # テキストフィールドをクリア
#         new_task.value = ""

#         # グローバル変数 te に "3939" を追加
#         global te
#         te = te + "3939"
        
#         # 画面上のテキストを更新
#         a.value = te
        
#         # 更新を反映
#         page.update()

#     # テキストフィールドとボタンを作成
#     new_task = ft.TextField(hint_text="What's needs to be done?")
#     a = ft.Text(te, size=25, weight=ft.FontWeight.W_500)  # 初期値として "kdkdk" を表示
    
#     # UIに追加
#     page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
#     page.add(a)

# ft.app(target=main)
