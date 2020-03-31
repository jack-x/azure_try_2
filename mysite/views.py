from django.shortcuts import render
from .models import Contact
# Create your views here.

from django.http import HttpResponse
import requests
import json
# def index(request):
#     return HttpResponse('Hello Boyz!!')


def index(request):
    if request.method == 'POST':
        first = request.POST.get('fname')
        print(first)
        last = request.POST.get('lname')
        print(last)

        r = requests.get("http://api.icndb.com/jokes/random?firstName={}&amp;lastName={}".format(first,last))
        print(r.text)
        json_data = json.loads(r.text)
        joke = json_data['value']['joke']

        joke = joke.replace("Norris",last)
        context = {'joker' : joke, 'firstname':first, 'lastname': last}
        print(json_data)
        print(joke)
        return render(request,'mysite/index.html',context)
    else:
        r = requests.get("http://api.icndb.com/jokes/random?firstName={}&amp;lastName={}".format("Chuck","Norris"))
        print(r.text)
        json_data = json.loads(r.text)
        joke = json_data['value']['joke']

        # joke = joke.replace("Norris",last)
        context = {'joker' : joke, 'firstname':'Chuck', 'lastname': 'Norris'}
        print(json_data)
        print(joke)
        return render(request,'mysite/index.html',context)


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        contactObject = Contact()

        contactObject.email = email
        contactObject.message = message
        contactObject.subject = subject
        contactObject.save()


        print(request.POST.get('email'))
        print("********** Adding details to contact table ************")
        print(email)
        print(message)
        print(subject)
        print("********************************************")
        return render(request,'mysite/thankyou.html')
    else:
        return render(request,'mysite/contact.html')

def portfolio(request):
    return render(request,'mysite/portfolio.html')
