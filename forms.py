from django import forms
from .models import *
from .widgets import DatePickerInput, TimePickerInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
# from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class SignUpForm(UserCreationForm):
    # ConfirmPassword = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'},))
    # widgets = forms.PasswordInput(attrs={'class':'form-control'})
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }
        
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
            

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class Hall(forms.ModelForm):
    class Meta:
        model = HallDetails
        fields = ['hallname', 'guests', 'halltype', 'hall_dec', 'hall_image']
        widgets = {
            'hallname': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'halltype': forms.TextInput(attrs={'class': 'form-control'}),
            'hall_dec': forms.TextInput(attrs={'class': 'form-control'}),
            # 'hall_image': forms.(attrs={'class': 'form-control'}),
        }


class HSlot(forms.ModelForm):
    class Meta:
        model = HallSlot
        fields = ['timeslot']
        widgets = {
            'timeslot': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FoodCat(forms.ModelForm):
    class Meta:
        model = CategoryFood
        fields = ['cname']
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Food(forms.ModelForm):
    class Meta:
        model = DetailFood
        fields = ['fname', 'fprice','fcategory']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'fprice': forms.NumberInput(attrs={'class': 'form-control'}),
            'fcategory': forms.Select(attrs={'class': 'form-control'}),
        }


class Contact(forms.ModelForm):
    query = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contactus
        fields = ['user', 'email', 'phone','query']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'query': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Book(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format='%Y%m%d'),
        input_formats=['%Y%m%d']
    )
    class Meta:
        model = Booking
        fields = ['date']





