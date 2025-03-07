import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render

from common.utils.email_service import send_email

from .models import Applicant
from .forms import JobApplicationForm

class JobAppView(CreateView):
    model = Applicant
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')
    
    def form_valid(self, form):
        data = form.cleaned_data
        content = f'''<p>Hey HR Manager!</p>
        <p>Job application received:</p>
        <ol>'''
        
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
            
        content += '</ol>'
            
            
        send_email('pandoraparigian@gmail.com', 'Application for Joke Writer', content)

    
        if 'email' in data and data['email']:
            send_email(data['email'], 'Your Job Application Received', 
                   '<p>Thank you for applying! We have received your application and will review it soon.</p>')

        return super().form_valid(form)

class JobAppThanksView(TemplateView):
    form = JobApplicationForm()
    template_name = 'jobs/thanks.html'

def job_application_view(request):
    form = JobApplicationForm()
    print("Form fields:", list(form.fields.keys()))  # Debugging step
    return render(request, 'applicant_form.html', {'form': form})
