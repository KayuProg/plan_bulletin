import asyncio

# 非同期関数の定義
async def task1(name):
    print(f"{name}さん、こんにちは")
    await asyncio.sleep(1)  # 1秒間非同期で待機
    print("こんにちは!")
    return name

async def task2(name):
    print(f"{name}さん、こんばんは")
    await asyncio.sleep(2)  # 2秒間非同期で待機
    print("こんばんは!")
    return name

# 非同期タスクを実行し、結果を収集するメイン関数
async def main():
    # asyncio.gatherを使用してtask1とtask2を同時に実行
    results = await asyncio.gather(
        task1("太郎"),  # task1に10を引数として渡す
        task2("花子"),  # task2に20を引数として渡す
    )
    print(results)  # 結果をリスト形式で出力

# イベントループを使用してmainを実行
asyncio.run(main())