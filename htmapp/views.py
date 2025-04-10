import requests
#: برای تحلیل و استخراج اطلاعات از HTML سایت.
from bs4 import BeautifulSoup 
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .forms import WordForm
from .models import portfolio,information
# Create your views here.

def index(request):
    pf = portfolio.objects.all()
    return render(request , 'index.html', {'pf':pf})


def registeration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # age = request.POST['age']
        password = request.POST['password']
        
        if (User.objects.filter(email=email).exists()):
            messages.info(request , 'Email already exists')
            return redirect('registeration')
        elif (User.objects.filter(username=username).exists()):
            messages.info(request , 'Username already exists')
            return redirect('registeration')
        else:
            user = User.objects.create_user(username=username , email=email , password=password)
            user.save()
            messages.info(request , 'User created')
            return redirect('login')
            
    else:    
        return render(request , 'registeration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username , password=password)
        
        if user:
            auth.login(request , user)
            return redirect('index')
        else:
            messages.info(request , 'Invalid credentials')
            return redirect('login')
    else:
        return render(request , 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def dict(request):
    word = None
    meaning = None
    main_meaning = None
    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            url = f"https://abadis.ir/?word={word}"
            response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
            soap = BeautifulSoup(response.text, 'html.parser')
            divs = soap.find('div', class_='lun boxBd boxMain')
            meaning = divs.find('b', string='معنی') if divs else None
            if meaning:
                raw_meanings = meaning.find_next('hr').previous_sibling.get_text(strip=True).split('،')
                main_meaning = [m.replace(':', '').strip() for m in raw_meanings if m.strip()]
            else:
                main_meaning = ["No meaning found"]
    context = {
        'form': form,
        'word': word,
        'meaning': main_meaning
    }
    return render(request , 'dict.html' , context=context)