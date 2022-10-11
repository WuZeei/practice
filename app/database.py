
from app import db

def fetch_todo() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from tasks;").fetchall()
    conn.close()
    todo_list = []
    # 將從資料庫裡的資料分別拆開
    for result in query_results:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)

    return todo_list

# 更新資料庫
def update_task_entry(task_id: int, text: str) -> None:
    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()

# 更新狀態
def update_status_entry(task_id: int, text: str) -> None:
    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()

# 新增資料
def insert_new_task(text: str) ->  int:
    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    # 新增完並取出顯示
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id

# 刪除資料
def remove_task_by_id(task_id: int) -> None:
    
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()

# 檢查帳號密碼
def get_accountandpassword(acc:str,wd:str) ->None:
    conn = db.connect()
    query = 'SELECT * from login where account ="{}" and password ="{}" limit 1;'.format(acc,wd)
    query_results = conn.execute(query)
    conn.close()
    if len(query_results.fetchall()) == 0:
        return False
    else:
        return True
