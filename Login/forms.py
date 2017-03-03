from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from Login.models import Item

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('is_deleted',)

class QuantityForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('quantity',)
