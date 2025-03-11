from datetime import datetime
from django.utils import timezone

import filetype
from private_storage.fields import PrivateFileField

from djangojokes.storage_backends import PrivateMediaStorage, PublicMediaStorage
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models

def avatar_saved(instance, filemame):
    return f"avatar/{instance.id}/{filemame}"

class MyAccount(models.Model):
    avatar = models.ImageField(upload_to= avatar_saved, storage=PublicMediaStorage())

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )

def validate_pdf(value):
    kind = filetype.guess(value)
    if not kind or kind.mime != 'application/pdf':
        raise ValidationError("That’s not a PDF file.")

class Job(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    EMPLOYMENT_TYPES = (
        (None, '--Please choose--'),
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
        ('contract', 'Contract work')
    )

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(help_text='A valid email address.')
    website = models.URLField(
        blank=True, validators=[URLValidator(schemes=['http', 'https'])]
    )
    employment_type = models.CharField(
        max_length=10, choices=EMPLOYMENT_TYPES, default='ft'
    )
    start_date = models.DateField(
        help_text='The earliest date you can start working.',
        validators=[validate_future_date],
        null=True,  # Allows null values for existing rows
        blank=True  # Allows blank fields for form validation
    )
    available_days = models.CharField(max_length=20, default="Please choose")
    desired_hourly_wage = models.DecimalField(
        max_digits=5, decimal_places=2, default=15.00
    )
    cover_letter = models.TextField(default="No cover letter provided")
    resume = PrivateFileField(
    upload_to='resumes', blank=True, help_text='PDFs only',
    validators=[validate_pdf]
    )
    confirmation = models.BooleanField(default=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.job})'
