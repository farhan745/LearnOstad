from django import forms
from .models import Employee,Position


class EmployeeForm(forms.ModelForm):
    gender_choices = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter employee name",
            }
        ),
        initial="None",
        help_text="Please enter a valid name.",
    )

    emp_salary = forms.IntegerField(
        min_value=0,
        max_value=10e5,
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "id": "emp_salary",
                "placeholder": "Salary",
            }
        ),
        label="Employee salary",
        initial=0,
        help_text="Please enter a valid salary.",
    )
    emp_score = forms.FloatField(
        label="Employee Score",
        min_value=0.0,
        max_value=100.0,
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "id": "emp_score",
                "placeholder": "Employee score",
            }
        ),
        initial=0,
        help_text="Please enter a valid score.",
    )
    is_employed = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id": "is_employed",
            }
        ),
        label="Is Employed",
    )
    '''
    #Date Fields for the employee
    employed_joining_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
            "id": "employed_joining_date",
            "placeholder": "Employed joining date",
        }),
        label='Enter Your Join Date'
    )
    '''
    employed_joining_date_joined=forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "class": "form-control",
            "type": "datetime-local",
            "id": "employed_joining_date_joined",
            "placeholder": "Employed joining date and time",
        }),
        label='Enter Your Join Date and Time',
        required=True,
    )
    emp_email = forms.EmailField(
        label="Employee Email",
        required=True,
        widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type":"email",
        'placeholder':'example@gmail.com'
        }),
    )
    
    emp_gender= forms.ChoiceField(
        choices = gender_choices,
        widget=forms.Select(attrs={
           "class": "form-control", 
        })
    )
    
    emp_files = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
                
            }
        ),
        label="Uploads Files",
        help_text="Text File"
        )
    emp_profile = forms.ImageField(
        label="Employee Profile",
        help_text="Photo File",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
                
                
            }
        )
    )
    
    
    emp_url = forms.URLField(
        label="Employee URL",
        
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "id": "emp_url",
                "placeholder": "Enter employee URL",
            }
        ),
        help_text="Please enter a valid URL."
    )
    
    #ManyToManyField 
    emp_position = forms.ModelMultipleChoiceField(
        label = "Employee Position",
        queryset= Position.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input",
                
            })
    )
    password = forms.CharField(
        max_length=50,
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter employee name",
            }
        ),
        initial="None",
        help_text="Please enter Password",
    
    )
        
    class Meta:
        model = Employee
        fields = [
            "emp_name",
            "emp_salary",
            "emp_score",
            "is_employed",
            "employed_joining_date_joined",
            "emp_email",
            "emp_gender",
            "emp_files",
            "emp_profile",
            "emp_url",
            "password",
            "emp_position",
            
            ]

