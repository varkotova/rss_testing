
// отправляем ajax-запрос на сервер
$("#check_name_btn").click(function () {
    $.ajax({
        type:"GET",

        url:"check_user_name/",

        data: {
            'user_name':$("#user_name_input").val(),
        },

        dataType: "text",

        cache: false,

        success: function (data) {
            if (data == 'ok') {
                console.log("ok");
            }
            else if (data == 'no') {
                console.log('no');

            }
        }
    });
});