from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from med_ease.models import Contact
from .forms import DjangoUserCreationForm, BookQueueForm
from django.utils.http import urlencode



# Create your views here.
def home(request):
    if request.session.get('message', None):
        message = request.session['message']
        context_variable = {'message':message}
        del request.session['message']
        return render(request, 'med_ease/home.html', context_variable)
    return render(request, 'med_ease/home.html')

def contact(request):
    context_variable = {}
    if request.session.get('message', None):
        message = request.session['message']
        context_variable['message'] = message
        del request.session['message']
    if request.method == 'POST': 
        fullname = request.POST['fullname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        message = request.POST['message']
        ins = Contact(fullname= fullname, email = email, phonenumber = phonenumber, message = message) # create the data
        ins.save() # save the data in the database
        request.session['message'] = 'Your enquiry has been registered'
        return redirect(request.path)
    return render(request, 'med_ease/contact.html', context_variable)

def about(request):
    return render(request, 'med_ease/about.html')

def signup(request):
    if request.method == 'GET':
        signup_form = DjangoUserCreationForm()
        context_variable = {'signup_form':signup_form}
        return render(request, 'med_ease/signup.html', context_variable)
    elif request.method == 'POST':
        signup_form = DjangoUserCreationForm(request.POST)
        if not signup_form.is_valid():
            context_variable = {'signup_form':signup_form}
            return render(request, 'med_ease/signup.html', context_variable)
        signup_form.save()
        login_url = reverse('login') + '?' + urlencode( {'next': reverse('med_ease:queue')} )
        return redirect(login_url)
        
@login_required
def queue(request):
    if request.method == 'GET':
        bookqueue_form = BookQueueForm()
        context_variable = {'bookqueue_form':bookqueue_form}
        return render(request, 'med_ease/queue.html', context_variable)
    elif request.method == 'POST':
        bookqueue_form = BookQueueForm(request.POST)
        if not bookqueue_form.is_valid():
            context_variable = {'bookqueue_form':bookqueue_form}
            return render(request, 'med_ease/queue.html', context_variable)
        bookqueue_form.save()
        request.session['message'] = 'Booking Successful, \nWe will get back to you shortly'
        return redirect(reverse('med_ease:home'))
        
        
    
        
    
        