# Generated by Django 5.1.6 on 2025-03-10 17:35

import djangojokes.storage_backends
import jobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', storage=djangojokes.storage_backends.PrivateMediaStorage(), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]
