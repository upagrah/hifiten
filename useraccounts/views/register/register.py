from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from .forms import UsersLoginForm,UsersRegisterForm
from django.http import HttpResponse,JsonResponse
from django import forms
from django.conf import settings
import sys
sys.path.insert(0,settings.BASE_DIR)
from utilities.validator import SpecialChars
from utilities.responses import SuccessRes,ErrorRes
from django.contrib.auth import authenticate, get_user_model
import traceback
import json
#from django.contrib.auth.models import User

User = get_user_model()
def register_post_validate(data):
	#print(self.data)
	#print(self["email"].value())
	required_keys=[
		"email",
		"confirmPassword",
		"username",
		"name",
		"password"
	]
	for key in required_keys:
		if(key not in data.keys()):
			raise forms.ValidationError(f"{key} not submitted")
	email = data["email"]
	confirmPassword = data["confirmPassword"]
	username = data["username"]
	name = data["name"]
	password = data["password"]

	print(email,confirmPassword,username,name,password)


	if(username and password and name and confirmPassword and email):
		if SpecialChars(username):
			raise forms.ValidationError('Only alphabets and numbers are allowed in username')
		if password != confirmPassword:
			error={
				'error_code':400,
				'error_message':"Entered passwords donot match",
				'error_data':''
			}
			raise forms.ValidationError(error['error_message'])
			#return ErrorRes(error)

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			error={
				'error_code':400,
				'error_message':"Email is already Registered",
				'error_data':''
			}
			raise forms.ValidationError(error['error_message'])

		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			error={
				'error_code':400,
				'error_message':f"User with username : {username} already registered",
				'error_data':''
			}
			raise forms.ValidationError(error['error_message'])

		#you can add more validations for password

		if len(password) < 8:
			error={
				'error_code':400,
				'error_message':f"Password must be greater than 8 charecters",
				'error_data':''
			}
			raise forms.ValidationError(error['error_message'])
	else:
		error={
				'error_code':400,
				'error_message':f"Required arguments are not present/passed in the field",
				'error_data':''
			}
		print(error)
		raise forms.ValidationError(error['error_message'])
def register_view(request):

	if(request.method=='GET'):
		return render(request, "accounts/register.html", {
			"title" : "Register",
		})
	elif(request.method=='POST'):
		try:
			print(request.body)
			data=json.loads(request.body)

			register_post_validate(data)
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
				'error_message':f'Internal Server Error #REG1 :{e}',
				'error_data':''
			}
			return ErrorRes(error)

		try:
			user=User.objects.create_user(username=data['username'], password=data['password'],email=data['email'],first_name=data['name'],is_active=False)
			password = data['password']
			user.set_password(password)
			user.save()
			data={
				'message':'You have been registered. Please activate by using the link on your email'
			}
			#new_user = authenticate(username = user.username, password = password)
			#login(request, new_user)
			#return redirect("/accounts/login")
			return SuccessRes(data)

		except Exception as e:
			#print(traceback.format_exc())
			error={
				'error_code':400,
				'error_message':f'Internal Server Error #REG2: {e} ',
				'error_data':''
			}
			return ErrorRes(error)



	else:
		error={
				'error_code':400,
				'error_message':f"This request is not valid for this page",
				'error_data':''
			}
		return ErrorRes(error)
