from django import forms
from django.forms import ModelForm
from .models import Department,City,CustomUser,QuizSession,Question,UserAnswer,Result,Question
from django.contrib.auth.forms import UserCreationForm

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department  
        fields = ['dept_name']

class CityForm(forms.ModelForm):
    class Meta:
        model = City  
        fields = ['city_name']  

       
class SessionForm(forms.ModelForm):
    end_time= forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        label='end_time'
    )
    start_time= forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        label='start_time'
    )
    class Meta:
        model =  QuizSession 
        fields = ['creator','user','subject', 'start_time','end_time']  
     

class QueForm(forms.ModelForm):
    class Meta:
        model = Question  
        fields = ['quiz_id','question_text','option1','option2','option3','option4','option5', 'correct_answer'] 


class CustomUserForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )
    date_of_joining = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label='Date of Joining'
    )
    department_choices = [(None, 'Select Department')]  # Empty choice
    department_choices += Department.objects.all().values_list()
    
    dept = forms.ModelChoiceField(
        # choices=department_choices,
        empty_label='Select Department',
        queryset=Department.objects.all(),
        label="Department",
        widget=forms.Select(attrs={'class': 'form-control'})  
    )

    city_choices = [(None, 'Select City')]  # Empty choice
    city_choices += City.objects.all().values_list()

    city = forms.ModelChoiceField(
        empty_label='Select City',
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})  

    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'dept',
            'city',
            'date_of_birth',
            'date_of_joining',
            # Add other fields as needed
        ]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class QuizQuestionForm(forms.ModelForm):
    selected_option = forms.ChoiceField(choices=[], widget=forms.RadioSelect, required=False)

    class Meta:
        model = Question
        fields = ['selected_option']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Get the instance of the question
        instance = kwargs.get('instance')
        
        # If the instance exists, populate choices for the selected_option field with the available options
        if instance:
            options = []
            # Construct choices based on option1 to option5 fields
            for i in range(1, 6):
                option_field = f'option{i}'
                option_value = getattr(instance, option_field)
                if option_value:
                    options.append((f'option{i}', option_value))
            self.fields['selected_option'].choices = options



