from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# JSON
import requests
import json


@api_view(['GET', 'POST'])
def sajili(request):
	if request.method == 'POST':
		data = json.loads(request.data)
		phone_number = data['phone_number']
		full_name = data['full_name']
		balance = int(data['balance'])
		pin = data['pin']
		try:
			sajili = Sajili.objects.create(
				full_name=full_name, phone_number=phone_number, balance=balance, pin=pin)
			if sajili:
				data = {"success": True}
				response = json.dumps(data)
				return Response(response)

		except Exception as e:
			print(e)
			data = {"success": False}
			response = json.dumps(data)
			return Response(response)

	return Response({})
