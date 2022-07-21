from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

#url name 'register'
#renders a register HTML page with a form
#after the user signs up, it redirects him to the 'login' page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            #adding a message 
            messages.success(request, f'Account successfuly created for {username}')
            
            return redirect('login')
    else:    
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
