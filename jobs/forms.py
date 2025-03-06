from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from .models import Job, Applicant

def validate_checked(value):
    if not value:
        raise ValidationError("Required.")

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )
class JobApplicationForm(forms.ModelForm):
    job_position = forms.ModelChoiceField(queryset=Job.objects.all())
    EMPLOYMENT_TYPES = (
        (None, '--Please choose--'),
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
        ('contract', 'Contract work')
    )

    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI')
    )

    YEARS = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False,
            widget=forms.URLInput(
                attrs={'placeholder':'https://www.example.com', 'size':'50'}
                ),
                validators=[URLValidator(schemes=['http', 'https'])]
                )
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)
    start_time = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(
            years=YEARS,
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'}
    )
    
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text='Check all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs = {'checked':True}
        )
    )

    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min':'10.00', 'max':'100.00', 'step':'.25'}
        )
    )

    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )

    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.',
        validators=[validate_checked]
    )

    class Meta:
        model = Applicant
        fields = (
            'first_name', 'last_name', 'email', 'website', 'employment_type',
            'start_date', 'available_days', 'desired_hourly_wage', 
            'cover_letter', 'confirmation', 'job')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
            'start_date': forms.SelectDateWidget(
                attrs = {
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = range(datetime.now().year, datetime.now().year+2)
            ),
            'desired_hourly_wage': forms.NumberInput(
                attrs = {'min':'10.00', 'max':'100.00', 'step':'.25'}
            ),
            'cover_letter': forms.Textarea(attrs={'cols': '100', 'rows': '5'})
        }
        error_messages = {
            'start_date': {
                'past_date': 'Please enter a future date.'
            }
        }