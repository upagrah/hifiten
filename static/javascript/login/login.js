var LoginApp = new Vue({
    el: '#login-app',
    data: {
        username: '',
        password: '',
        csrf_token: '',
    },
    methods: {
        submitLogin: function() {
            //console.log("USERNAME IS :" + this.csrf_token);
            var userObject = {
                "username": this.username,
                "password": this.password,

            }
            $.ajax({
                type: "POST",
                url: '/accounts/login/',
                data: JSON.stringify(userObject),
                headers: { "X-CSRFToken": token },
                contentType: "application/json;",
                dataType: "json",
                success: function(responseData, textStatus, jQxhr) {
                    //alert("You have been registered, activate your account for logging in")
                    window.location = '/';
                },
                error: function(responseData, textStatus, jQxhr) {
                    //console.log(responseData.responseJSON);
                    alert(responseData.responseJSON['error_message']);
                    //alert("Error while registering with status :" + textStatus + "\n with error : > \n " + errorThrown);
                }
            });
        }
    }
});