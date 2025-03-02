from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path

# 読み取り権限を指定
SCOPES = ["https://www.googleapis.com/auth/tasks"]

json_pass="./get_info/jsons/tasks_token.json"

def main():
    creds = None#認証情報を格納する変数
    # トークンファイルを確認して認証情報をロード
    if os.path.exists(json_pass):#.jsonが存在するかの確認
        creds = Credentials.from_authorized_user_file(json_pass, SCOPES)
    
    # 認証情報が無効な場合、ログインプロセスを実行
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:#tokenの期限切れ確認
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("./jsons/parent.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open(json_pass, "w") as token:
            token.write(creds.to_json())

    try:
        # Google Tasks APIのサービスを初期化
        service = build("tasks", "v1", credentials=creds)#Google tasks APIを使うためのオブジェクト



        # タスクリストのIDを指定してタスクを取得
        tasklist_id = "MTQzMjUyMTY0MTk3NDc0NDg1ODU6MDow"  # ここに取得したタスクリストIDを入れる
        results = service.tasks().list(tasklist=tasklist_id).execute()
        tasks = results.get("items", [])
        # print(tasks)

        if not tasks:
            print("タスクリスト内にタスクはありません。")
            return

        print("タスク一覧:")
        for task in tasks:
            print(f"{task['title']} (Due: {task['due']})")
    except HttpError as err:
        print(f"エラーが発生しました: {err}")

if __name__ == "__main__":
    main()

