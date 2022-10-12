
from app import db

def fetch_todo(account: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from tasks where account = "{}";'.format(account)).fetchall()
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
def update_task_entry(task_id: int, text: str, account:str) -> None:
    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {} and account = "{}";'.format(text, task_id,account)
    conn.execute(query)
    conn.close()

# 更新狀態
def update_status_entry(task_id: int, text: str, account: str) -> None:
    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {} and account = "{}";'.format(text, task_id,account)
    conn.execute(query)
    conn.close()

# 新增資料
def insert_new_task(text: str,account: str) ->  int:
    conn = db.connect()
    query = 'Insert Into tasks (task, status,account) VALUES ("{}", "{}","{}");'.format(
        text, "Todo",account)
    conn.execute(query)
    # 新增完並取出顯示
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id

# 刪除資料
def remove_task_by_id(task_id: int,account: str) -> None:
    
    conn = db.connect()
    query = 'Delete From tasks where id={} and account = {};'.format(task_id,account)
    conn.execute(query)
    conn.close()

# 檢查帳號密碼
def get_accountandpassword(acc:str,wd:str) ->None:
    conn = db.connect()
    query = 'SELECT * from login where account ="{}" and password ="{}";'.format(acc,wd)
    query_results = conn.execute(query)
    conn.close()
    return_data = False
    if query_results.rowcount == 0:
        return return_data
    else:
        return_data = True
        return return_data
