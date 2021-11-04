from django.urls import path
from .import views

app_name = "ussd"

urlpatterns = [
	path('', views.index,name='index'),
]
