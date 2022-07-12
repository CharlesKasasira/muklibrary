from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ( 
  ListView, 
  DetailView,
)

from .models import Book

# Books
class BookListView(ListView):
  model = Book 
  queryset = Book.objects.all().order_by("-created_at")


class BookDetailView(DetailView):
  model = Book 

# End of Books

@login_required(login_url='login')
def home(request):
	return render(request, 'authenticate/home.html', {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Successful logged in!'))
			return redirect('book-list')

		else:
			messages.error(request, ('Failed: check your password or username'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

@login_required(login_url='login')
def logout_user(request):
	logout(request)
	messages.success(request, ('Successful logged out!'))
	return redirect('login')

def register_user(request):
	if request.user.is_anonymous:
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username=username, password=password)
				login(request, user)
				messages.success(request, ('Welcome: Successful registered!'))
				return redirect('book-list')

	else:
		return redirect("book-list")
	form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'authenticate/register.html', context)
