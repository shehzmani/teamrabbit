from django.shortcuts import render
from clubs.forms import SignUpForms
from.forms import SignUpForm

# Create your views here.
def home(request):
   return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm()
    return render(request, 'sign_up.html',{'form':form})

def create_club(request):
    if request.method == 'POST':
        form = CreateClubForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                Post.objects.create(
                owner = request.User,
                name = form.cleaned_data['name']
                location = form.cleaned_data['location']
                description = form.cleaned_data['description']
                )
            return redirect('home')
        else:
            messages.error(request, "User has to login in order to create a club")
    else:
        form = forms.CreateClubForm()
    return render(request, 'create_club.html', {'form': form})
