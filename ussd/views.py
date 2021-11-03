from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import requests
import re
from decimal import Decimal
from .models import *


def calculate(amount, tofauti, ongezeko):
	total = (tofauti * Decimal(ongezeko)) + tofauti + amount
	return round(Decimal(total), 2)

def T(tofauti, ongezeko):
	T = (tofauti * Decimal(ongezeko)) + tofauti
	return round(Decimal(T), 2)

@csrf_exempt
def index(request):
	if request.method == 'POST':
	   	
		#Collected Data
		text = request.POST.get('text')
		phone_number = request.POST.get('phoneNumber')

		response = ""

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
		
		elif text.startswith("2*0") and len(text) == 12: 
			response = "CON Ingiza kiasi \n"

		elif text.startswith("2*0") and text.count("*") == 2:
			receiver = text[2:12]
			amount = re.sub("2\*.+\*", '', text)
			amount = Decimal(amount)
			print(receiver)
			if 5000 > amount:
				response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 50,00/="
			if 5000 <= amount <= 6000:
				answer = calculate(amount, 375, 0.001)
				t = T(375, 0.001)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 6001 <= amount <= 7000:
				answer = calculate(amount, 475, 0.008)
				t = T(475, 0.008)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 7001 <= amount <= 8000:
				answer = calculate(amount, 575, 3.7)
				t = T(575, 3.7)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 8001 <= amount <= 9000:
				answer = calculate(amount, 600, 3.8)
				t = T(600, 3.8)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 9001 <= amount <= 10000:
				answer = calculate(amount, 650, 4.3)
				t = T(650, 4.3)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 10001 <= amount <= 11000:
				answer = calculate(amount, 750, 5.1)
				t = T(750, 5.1)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 11001 <= amount <= 12000:
				answer = calculate(amount, 800, 6.2)
				t = T(800, 6.2)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 12001 <= amount <= 13000:
				answer = calculate(amount, 900, 7.4)
				t = T(900, 7.4)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

		elif text.startswith("2*"): 
			response = "END Namba uliyoingiza si sahihi \n"

		else:
			response = "END Chaguo lako sio sahihi."    
			
		return HttpResponse(response)


