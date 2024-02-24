from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import foodDiet, medicalRecord, Contact
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, medicalRecordForm
from .script import drug_name,get_dietd
from datetime import datetime
diet = []
med =[]

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
            messages(request, 'Username must be under 10 characters')

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
    global diet
    global med
    drug_names = request.session.get('drug_names', [])  # Initialize drug name information

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'upload':
            image = request.FILES.get('image')
            drug_items = drug_name(image)
            med.extend(drug_items)  # Assuming the drug name is stored in good_items
            request.session['drug_name'] = drug_names
            return render(request, 'upload.html', {'med': med})
        
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            good, bad = drug_names(image)
            return render(request, 'food.html', {'good': good, 'bad': bad})
        
    else:
       
        form = ImageUploadForm()
        med = []
    
    return render(request, 'upload.html', {'form': form, 'med':med})

def getdiet(request):
    global med
    good,bad = get_dietd(med)
    
    diet_plan = foodDiet.objects.create(good_foods=good, bad_foods=bad)
    return render(request, 'food.html', {'good': good, 'bad': bad})

def showdiet(request):
    diet_plan = foodDiet.objects.last()
    if diet_plan:
        to_consume = diet_plan.good_foods
        to_consume = to_consume.replace("'","")
        to_consume = to_consume.replace("[","")
        to_consume = to_consume.replace("]","")
        to_consume = to_consume.split(",")
        
        not_to_consume = diet_plan.bad_foods
        not_to_consume = not_to_consume.replace("'","")
        not_to_consume = not_to_consume.replace("[","")
        not_to_consume = not_to_consume.replace("]","")
        not_to_consume = not_to_consume.split(",")
        
    else:
        to_consume = ' '
        not_to_consume = ''
    return render(request, 'diet.html', {'to_consume': to_consume, 'not_to_consume': not_to_consume})


def showMedical(request):
    if request.method == 'POST':
        try:
            form = medicalRecordForm(request.POST, request.FILES)
            if form.is_valid(): 
                form.save() 
                return render(request, 'medical.html')  
        except Exception as e:
            return render(request, 'medical.html', {'error_message': str(e)})
    else:
        form = medicalRecordForm()
    return render(request, 'medical.html', {'form': form})

def medicalreport(request):
    medical_records = medicalRecord.objects.filter(user=request.user)
    return render(request, 'medical_record.html', {'medical_records': medical_records})

def success(request):
    return render(request, 'sucsess.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')
    return render(request, 'contactus.html')