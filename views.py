from django.shortcuts import render
from django.contrib.auth.models import User as myuser, auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from tree.models import User, registration, loggedin #models.py
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

@csrf_exempt
def login(request):

	if request.method == "POST":

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			print("successfull")
			return redirect('add')
		else:
			messages.info(request, 'Invalid credentials')
			return redirect('login')
	else:

	
		return render(request, 'login.html')

@csrf_exempt
def home(request):
	return render(request, 'home.html')

# def dashboardView(request):
# 	return render(request, 'dashboard.html')
@csrf_exempt
def register(request):
	
	if request.method == "POST":
		# form = registration(request.POST or None)
		username = request.POST['username']
		password = request.POST['password']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		# birthday = request.POST.get('birthday')
		# gender = request.POST.get('gender')
		# email = request.POST.get('email')
		# phone = request.POST.get('phone')
		if registration.objects.filter(username=username).exists():
			messages.info(request,"{Sorry username taken}")
			# print("username taken")
			return redirect('register')
		else:
			user = registration(username=username, password=password, first_name=first_name, last_name=last_name) #birthday=birthday, gender=gender, email=email, phone=phone)
			user.save()
			print("user created")
			return redirect('login')

	else:

		return render(request, 'register.html')

@csrf_exempt
def addperson(request):

	if request.method == "POST":

		firstname = request.POST['firstname']
		Surname = request.POST['Surname']
		gender = request.POST['gender']
		birthdate = request.POST['birthdate']
		relation = request.POST['relation']

		
		user = User(firstname=firstname, Surname=Surname, gender=gender, birthdate=birthdate, relation=relation)
	# if user.is_valid():
        # form.save()
		user.save()
		return redirect('successfull')

	return render(request, 'add.html')


@csrf_exempt
def successfull(request):

	#return redirect('home')
	return render(request, 'sucessfull.html')




def logout(request):
	# 
	auth.logout(request)
	print("hello")
	return redirect('home')
