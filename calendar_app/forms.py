from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task1,Task2,Task3
from django.utils import timezone
from django.forms import TextInput
 
#Taskform1 for Task1,Taskform2 for Task2,TaskForm3 for Task3

class RedirectForm(forms.Form):
    redirect_to = forms.ChoiceField(choices=[
        ('Department1', 'Department1'),
        ('Department2', 'Department2'),
        ('Department3', 'Department3'),
    ])
    
class TaskForm1(forms.ModelForm):
    class Meta:
        model = Task1
        fields = ['date','time', 'title', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description':forms.Textarea(attrs={'rows':9,'cols':30}),
          
            
        }


class TaskForm2(forms.ModelForm):
    class Meta:
        model = Task2
        fields = ['date','time', 'title', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description':forms.Textarea(attrs={'rows':9,'cols':30}),
          
            
        }

class TaskForm3(forms.ModelForm):
    class Meta:
        model = Task3
        fields = ['date','time', 'title', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description':forms.Textarea(attrs={'rows':9,'cols':30}),
          
            
        }        

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)





class MonthYearForm(forms.Form):
    MONTH_CHOICES = [
        (1, 'January'), (2, 'February'), (3, 'March'),
        (4, 'April'), (5, 'May'), (6, 'June'),
        (7, 'July'), (8, 'August'), (9, 'September'),
        (10, 'October'), (11, 'November'), (12, 'December')
    ]
    
    YEAR_CHOICES = [(year, year) for year in range(2000, timezone.now().year + 1)]
    
    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
