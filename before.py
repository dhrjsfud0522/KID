import flet as ft
from supabase import create_client, Client

URL = "https://woisajcavsxqocjaaajl.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvaXNhamNhdnN4cW9jamFhYWpsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4ODE3NjA4NywiZXhwIjoyMDAzNzUyMDg3fQ.GEZez1dA6vgg6YBfmogQ8IAom12vbtZa_zRhnYZS6qU"


def supa():
    """supabase 클라이언트 생성 함수"""
    return create_client(URL, KEY)

def main(page:ft.Page):
    page.title = "flet"
    

    def 버튼클릭 (e):
        print("클릭", field.value)
        #데이터베이스로 저장
        supabase.table("name_table").insert({"name":field.value}).execute()
        name_rander()
        #n = ft.Text(field.value)
        #col.controls.append(n)

        field.value = ""
        page.update()

    txt = ft.Text("저리가세요", size = 40)
    field = ft.TextField(hint_text = "아무것도 입력하지 마세요")
    btn = ft.TextButton("누르지 마세요", on_click = 버튼클릭)
    
    row = ft.Row()
    col = ft.Column()
    #데이터베이스에서 텍스트 불러오기
    supabase = supa()


    def name_rander():
        r = supabase.table("name_table").select("*").limit(1).execute()
        for i in range(len(col.controls)):
            col.controls.pop

        for info in r.data: #데이터베이스 순회
            t = ft.Text(info["name"] + "님 안녕하세요", size = 25)
            col.controls.append(t)
    name_rander()
    page.add(col)
    page.add(txt)
    page.add(field)
    page.add(btn)
    page.update()

ft.app(target = main)