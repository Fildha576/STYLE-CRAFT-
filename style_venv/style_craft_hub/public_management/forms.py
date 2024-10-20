from django import forms
from . models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 90%;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 90%;'}))

    # Clean method if you need to perform additional cleaning/validation
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        


              
     
class RegisterForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['name','email','password','contact','address']
        
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "email" : forms.EmailInput(attrs={'class':'form-control'}),
            "contact" : forms.TextInput(attrs={'class':'form-control','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'form-control'}),
            "password" : forms.PasswordInput(attrs={'class':'form-control'}),
             }


class TRegisterForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['name','email','password','contact','address','license','id_proof','location']
        
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "email" : forms.EmailInput(attrs={'class':'form-control'}),
            "contact" : forms.TextInput(attrs={'class':'form-control','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'form-control'}),
            "license" : forms.TextInput(attrs={'class':'form-control'}),
            "password" : forms.PasswordInput(attrs={'class':'form-control'}),
            "location" : forms.TextInput(attrs={'class':'form-control'}),
             }
       

class ProductForm(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = ['fabric']
        
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "email" : forms.EmailInput(attrs={'class':'form-control'}),
            "contact" : forms.TextInput(attrs={'class':'form-control','maxlength':'10'}),
            "address" : forms.TextInput(attrs={'class':'form-control'}),
            "license" : forms.TextInput(attrs={'class':'form-control'}),
            "password" : forms.PasswordInput(attrs={'class':'form-control'}),
            "location" : forms.TextInput(attrs={'class':'form-control'}),
             }
       