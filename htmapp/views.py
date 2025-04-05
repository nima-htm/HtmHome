import requests
#: برای تحلیل و استخراج اطلاعات از HTML سایت.
from bs4 import BeautifulSoup 
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WordForm
# Create your views here.

def index(request):
    return render(request , 'index.html')


def login(request):
    return render(request , 'login.html')


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