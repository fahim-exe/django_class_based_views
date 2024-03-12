from django.urls import path
from .views import HomeView, ThankYou

app_name = 'classroom'

#domain.com/classroom
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('thank_you/', ThankYou.as_view(), name="thankyou")
]


