from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm

# Create your views here.

def userloguin(request):
	if request.user.is_authenticated():
		return redirect('/admin')

	if request.method == 'POST':

		if 'register_form' in request.POST:
			user_to_register = RegisterForm(request.POST or None)
			
			if user_to_register.is_valid():
				instance = user_to_register.save(commit=False)
				instance.save()
				logIn(request, user_to_register.cleaned_data['email'], user_to_register.cleaned_data['password'])
				
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST or None)

			if login_form.is_valid():
				logIn(request, login_form.cleaned_data['email'], login_form.cleaned_data['password'])
	else:
		user_to_register = RegisterForm()
		login_form = LoginForm()

	return render(request, 'login.html', {'register' : user_to_register, 'login_form' : login_form})

def logIn(request, email, password):
	#import ipdb; ipdb.set_trace()
	user = authenticate(email=email, password=password)

	if user is not None:
		#import ipdb; ipdb.set_trace()
		if user.is_active:
			#import ipdb; ipdb.set_trace()
			login(request, user)
			return redirect('/admin')