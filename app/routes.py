from cgitb import reset
from this import d
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    # 接收刪除資料的請求
    data = request.get_json()

    try:
        db_helper.remove_task_by_id(task_id,data['account'])
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    # 接收更新的請求

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"],data['account'])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    # 接收新增目標
    data = request.get_json()
    db_helper.insert_new_task(data['description'],data['account'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    global current
    global account
    account = data['account']
    current = db_helper.get_accountandpassword(data['account'], data['password'])
    if current == True:
        return index()
    else:
        result = {'success': current}
        return jsonify(result)


@app.route("/index")
def index():
    # 返回呈現主頁

    if current == True:
        items = db_helper.fetch_todo(account)
        return render_template("index.html", items=items)
    else:
        return render_template("login.html")


@app.route("/logout", methods=['POST'])
def logout():
    # 登出
    data = request.get_json()
    global current
    current = data['status']
    return render_template('login.html')


@app.route("/")
def homepage():
    # 登陸頁面
    # items = db_helper.fetch_todo()
    # return render_template("index.html", items=items)
    return render_template("login.html")
