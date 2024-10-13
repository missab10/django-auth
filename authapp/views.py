from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('dashboard') # Redirect to a success page, such as 'home'
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)  # Reinitialize form for GET requests

    return render(request, 'auth/register.html', {'form': form}) 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Pass request and POST data
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to the dashboard or any other page
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)  # Initialize a blank form for GET requests

    return render(request, 'auth/login.html', {'form': form}) 

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
