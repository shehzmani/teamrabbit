from django.shortcuts import render
from clubs import forms
from clubs.models import Club
from clubs.forms import SignUpForms
from.forms import SignUpForm
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
   return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm()
    return render(request, 'sign_up.html',{'form':form})

def create_club(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.username
            form = forms.CreateClubForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name'),
                locations = form.cleaned_data.get('location'),
                description = form.cleaned_data.get('description'),
                post = Club.objects.create(name=name, location=location, description=description)
                return redirect('create_club')
            else:
                return render(request, 'create_club.html', {'form': form})
        else:
            return redirect('login')
    else:
        return HttpResponseForbidden()
