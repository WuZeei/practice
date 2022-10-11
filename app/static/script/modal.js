$(document).ready(function () {

    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) 
        const taskID = button.data('source') 
        const content = button.data('content') 
        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        // 取得ID和詳細資訊
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        const passdata = $('#task-modal').find('.form-control').val();
        $.ajax({
            type: 'POST',
            // 分建立或是修改
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': passdata
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        // 刪除資料
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        // 取得當前狀態
        const state = $(this)
        const tID = state.data('source')
        let new_state = "Todo"
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});