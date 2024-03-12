from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from classroom.forms import ContactForm

# Create your views here.

# def myHome(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    #this is not a template.html
    success_url = "classroom/thankyou"

    #success url
    #what to do with form?
