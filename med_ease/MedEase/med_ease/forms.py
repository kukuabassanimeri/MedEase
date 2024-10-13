from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import BookQueue

class DjangoUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email') + UserCreationForm.Meta.fields 
class BookQueueForm(ModelForm):
    class Meta:
        model = BookQueue
        fields = ['Fullname', 'Phonenumber', 'Email', 'Message']