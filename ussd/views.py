from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json


@csrf_exempt
def index(request):
    if request.method == 'POST':
       	
        #Collected Data
        text = request.POST.get('text')
        phone_number = request.POST.get('phoneNumber')

        response = ""

        #account = Account.objects.filter(phone=phone_number).first()
        if text == "":
            response = "CON  Menu   \n"
            response += "1. Sajili \n"
            response += "2. Tuma Pesa \n"
            response += "00. Exit \n"
       
        elif text == "1":
            print(text)
            response = "CON Menu > Sajili \n"
            response += "Ingiza namba ya simu  \n"
        elif text == "2":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"
        else:
            response = "END Chaguo lako sio sahihi."    
            
        return HttpResponse(response)


