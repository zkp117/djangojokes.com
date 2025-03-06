from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Applicant  # Make sure this is present
from .forms import JobApplicationForm  # If using a form
from common.utils.email_service import send_email  # If you have a custom email function

from django.views.generic import TemplateView

class JobAppThanksView(TemplateView):
    template_name = "jobs/job_app_thanks.html"
class JobAppView(CreateView):
    model = Applicant
    template_name = 'jobs/applicant_form.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'pandoraparigian@gmail.com'
        subject = 'Application for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'

        send_email(to, subject, content)
        
        response = super().form_valid(form)  # Save the form
        connection.close()  # Explicitly close DB connection
        return response
