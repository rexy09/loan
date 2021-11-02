from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json
import re
from decimal import Decimal
from .models import *


def calculate(amount, tofauti, ongezeko):
	total = (tofauti * Decimal(ongezeko)) + tofauti + amount
	return round(Decimal(total), 2)


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
	   
		elif text == "1":
			print(text)
			response = "CON Menu > Sajili \n"
			response += "Ingiza namba ya simu  \n"
			
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
			if 5000 <= amount <= 6000:
				answer = calculate(amount, 375, 0.001)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=375, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 6001 <= amount <= 7000:
				answer = calculate(amount, 475, 0.008)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=475, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 7001 <= amount <= 8000:
				answer = calculate(amount, 575, 3.7)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=575, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 8001 <= amount <= 9000:
				answer = calculate(amount, 600, 3.8)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=675, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 9001 <= amount <= 10000:
				answer = calculate(amount, 650, 4.3)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=650, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

			elif 10001 <= amount <= 11000:
				answer = calculate(amount, 750, 5.1)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=750, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 11001 <= amount <= 12000:
				answer = calculate(amount, 800, 6.2)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=800, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"


			elif 12001 <= amount <= 13000:
				answer = calculate(amount, 900, 7.4)
				try:
					obj = TumaPesa.objects.create(no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=900, jumla=answer)
					response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
				except Exception as err:
					print(err)
					response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

		elif text.startswith("2*"): 
			response = "END Namba uliyoingiza si sahihi \n"

		else:
			response = "END Chaguo lako sio sahihi."    
			
		return HttpResponse(response)


