from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .script import drug_name


# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpw = request.POST['confirmpw']

        if User.objects.filter(username = username):
            messages.error(request, "Username already exist! Please try again!!")
            return redirect('home')

        if User.objects.filter(email = email):
            messages.error(request, 'Email already in use')
            return redirect('home')
        
        if len(username)>10:
            messages(request, 'username must be under 10 characters')

        if password != confirmpw:
            messages.error(request, "Password didn't match!")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, " Your account has been successfully created!! We have sent you a confirmation mail in you email-id")


        return redirect('signin')
    

    return render(request, "signup.html")

def signin(request): 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)

        if user is not  None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname': fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')


def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            good_items, bad_items, drug_items = drug_name(image)
            return render(request, 'food.html', {'good': good_items, 'bad': bad_items})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

                                                                                                      
