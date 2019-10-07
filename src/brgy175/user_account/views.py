from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.conf import settings


# Create your views here.

def register(request):
	if request.method == 'POST':
		if 'SignUp' in request.POST:
			global form_register
			form_register = UserRegisterForm(request.POST)
			if form_register.is_valid():
				form_register.save()

		elif 'SignIn' in request.POST:
			global form_login
			form_login = LoginForm(request.POST)
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect((settings.LOGIN_REDIRECT_URL))
			
	
	else:	
		form_register = UserRegisterForm()
		form_login = LoginForm()

	context = {
		'form_l': form_login,
		'form_r': form_register,
	}
		
		
	return render(request, 'user_account/login.html', context)

