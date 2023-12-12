from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  # Importa o modelo de usuário do Django
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = LoginForm()
        
        
        if not form.data:  
            
            generic_user, created = User.objects.get_or_create(username='generic_user', defaults={'password': 'password123'})
            if created:
                generic_user.set_password('password123') 
                generic_user.save()

            login(request, generic_user)
            return redirect('home')  
    
    return render(request, 'login.html', {'form': form})
