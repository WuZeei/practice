$(document).ready(function () {
    $('#submit-login').click(function () {
        const loginaccount = $('#login-account').val()
        const loginpassword = $('#login-password').val()
        if (loginaccount || loginpassword == '') {
            $('#myModal').modal('show')
            // location.reload();
        }
        console.log($('#login-account').val())
        $.ajax({
            type: 'POST',
            url: '/login_for',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'account': loginaccount,
                'password': loginpassword
            }),
            success: function (res) {
                console.log(res)
                if (res = true) {
                    console.log(res.response)
                    // location.reload();
                } else {
                    $('#myModal').modal('show')
                    location.reload();
                }
            },
            error: function () {
                console.log('Error');
            }
        })
    })
})