from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path

# 読み取り権限を指定
SCOPES = ["https://www.googleapis.com/auth/tasks"]
#うまく実行されないとき
#google.auth.exceptions.RefreshError: ('invalid_scope: Bad Request', {'error': 'invalid_scope', 'error_description': 'Bad Request'})
#というエラーが出たとき次のやつで実行するとよさそう．
# SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]


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
            flow = InstalledAppFlow.from_client_secrets_file("./get_info/jsons/parent.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open(json_pass, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("tasks", "v1", credentials=creds)

        # Call the Tasks API
        results = service.tasklists().list(maxResults=10).execute()
        items = results.get("items", [])

        if not items:
            print("No task lists found.")
            return

        print("Task lists:")
        for item in items:
            print(f"{item['title']} ({item['id']})")
    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()

