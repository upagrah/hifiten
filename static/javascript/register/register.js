var RegistrationApp = new Vue({
    el: '#registration-app',
    data: {
        username: '',
        password: '',
        email: '',
        name: '',
        confirm_password: '',
        csrf_token: '',
    },
    methods: {
        submitRegister: function() {
            //console.log("USERNAME IS :" + this.csrf_token);
            var userObject = {
                "username": this.username,
                "password": this.password,
                "email": this.email,
                "name": this.name,
                "confirmPassword": this.confirm_password,
            }
            $.ajax({
                type: "POST",
                url: '/accounts/register/',
                data: JSON.stringify(userObject),
                headers: { "X-CSRFToken": token },
                contentType: "application/json;",
                dataType: "json",
                success: function(responseData, textStatus, jQxhr) {
                    alert("You have been registered, activate your account for logging in")
                    window.location = '/accounts/login';
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