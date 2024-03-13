from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from classroom.models import Teacher
from django.urls import reverse, reverse_lazy

from classroom.forms import ContactForm

# Create your views here.

# def myHome(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'



class TeacherCreateView(CreateView):
    model = Teacher

    #modef_form.html

    fields = "__all__"
    success_url = reverse_lazy("classroom:thankyou")


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    #this is not a template.html
    success_url = reverse_lazy("classroom:thankyou")

    #success url
    #what to do with form?

    def form_valid(self, form):
        print(form.cleaned_data)

        #form.save
        return super().form_valid(form)
    

