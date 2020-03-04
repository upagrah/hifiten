from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def home_view(request):
    if(request.method=='GET'):
        return render(request, "home.html", {
        "title" : "Register",
        })
    else:
        error={
            'error_code':400,
            'error_message':f"This request is not valid for this page",
            'error_data':''
        }
        return ErrorRes(error)