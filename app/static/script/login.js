$(document).ready(function () {
    $('#submit-login').click(function () {
        const loginaccount = $('#login-account').val()
        const loginpassword = $('#login-password').val()
        if ((loginaccount && loginpassword) == '') {
            $('#myModal').modal('show')
            // location.reload();
        } else {
            console.log($('#login-account').val())
            $.ajax({
                type: 'POST',
                url: '/login',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'account': loginaccount,
                    'password': loginpassword,
                }),
                success: function (res) {
                    if (res['success'] == false) {
                        $('#myModal').modal('show')
                    } else {
                        sessionStorage.setItem('account', loginaccount)
                        location.replace("index")
                        // console.log(res)
                    }
                },
                error: function () {
                    console.log('Error');
                }
            })
        }
    })
})