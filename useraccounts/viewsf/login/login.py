from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, get_user_model
from django import forms
from django.conf import settings
import sys
sys.path.insert(0,settings.BASE_DIR)
from utilities.responses import SuccessRes,ErrorRes 
import json



def login_post_validate(data):
    required_keys=[
        "username",
        "password"
    ]
    for key in required_keys:
        if(key not in data.keys()):
            raise forms.ValidationError(f"{key} not submitted")
    username = data['username']
    password = data['password']

    if username and password:
        user = authenticate(username = username, password = password)
        if not user:
            raise forms.ValidationError('Username & Password combination incorrect, please check again')
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError("User is no longer active")
    else:
        raise forms.ValidationError("please send all the required parameters")

def login_view(request):
    if(request.method=='GET'):
        return render(request, "accounts/login.html", {
            "title" : "Login",
        })
    elif(request.method=='POST'):
        try:
            print(request.body)
            data=json.loads(request.body)

            login_post_validate(data)
        except forms.ValidationError as e:
            error={
                'error_code':400,
                'error_message':f'Validation error :{e}',
                'error_data':''
            }
            return ErrorRes(error)
        except Exception as e:
            #print(traceback.format_exc())
            error={
                'error_code':400,
                'error_message':f'Internal Server Error #LOG1 :{e}',
                'error_data':''
            }
            return ErrorRes(error)
        try:
            username = data['username']
            password = data['password']
            user = authenticate(username = username, password = password)
            login(request, user)

            return SuccessRes({})

        except Exception as e:
        #print(traceback.format_exc())
            error={
                'error_code':400,
                'error_message':f'Internal Server Error #LOG2: {e} ',
                'error_data':''
            }
            return ErrorRes(error)

from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")