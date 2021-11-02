from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests


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
            response += "Ingiza namba ya simu \n"
        elif text.startswith("1") and text.count("*")==1:
            print(text)
            response = "CON Ingiza Jina lako kamili \n"
        elif text.startswith("1") and text.count("*") == 2:
            print(text)
            response = "CON Ingiza Balance \n"
        elif text.startswith("1") and text.count("*") == 3:
            print(text)
            response = "CON Ingiza Pin \n"
        elif text.startswith("1") and text.count("*") == 4:
            print(text)
            text_data = text.split('*')
            print(text_data)

            url = 'https://571f-41-75-223-25.ngrok.io/ussd/sajili/'
            send_data = {
                'phone_number': text_data[1], 'full_name': text_data[2], 'balance': text_data[3], 'pin': text_data[4], }
            send_data = json.dumps(send_data)
            try:
                resp = requests.post(url, json=send_data)
                print(resp.json())
                json_data = resp.json()
                data = json.loads(json_data)

                if data['success'] == True:
                    response = "END Ahsante usajili umekamilika. \n"
                else:
                    response = f"END Samahani usajili haujakamilika jaribu tena."
            except Exception as e:
                print(e)
                response = f"END Ndugu mteja, kuna tatizo la kimtandao kwa sasa. Tafadhali jaribu tena baadae."

        elif text == "2":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"
        else:
            response = "END Chaguo lako sio sahihi."    
            
        return HttpResponse(response)


