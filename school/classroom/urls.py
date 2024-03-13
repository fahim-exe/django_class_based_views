from django.urls import path
from .views import (HomeView, ThankYou, ContactFormView, TeacherCreateView, TeacherListView)

app_name = 'classroom'

#domain.com/classroom
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('thank_you/', ThankYou.as_view(), name="thankyou"),
    path("contact/", ContactFormView.as_view(), name='contact'),
    path("teacher/", TeacherCreateView.as_view(), name='teacher'),
    path("teacherlist/", TeacherListView.as_view(), name="teacherlist"),

]


