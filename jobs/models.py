from django.db import models

# Create your models here.
from django.db import models

class Applicant(models.Model):
    # Define fields for your Applicant model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    # Other fields...

    def __str__(self):
        return self.name