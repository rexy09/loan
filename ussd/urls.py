from django.urls import path
from .import views
from . import api

app_name = "ussd"

urlpatterns = [
	path('', views.index,name='index'),

	# API
	path('sajili/', api.sajili, name='sajili'),

]
