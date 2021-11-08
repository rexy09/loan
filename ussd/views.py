from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import requests
import re
from decimal import Decimal
from .models import *


def calculate(amount, tofauti, ongezeko):
    total = (tofauti * Decimal(ongezeko)) + tofauti + amount
    return round(Decimal(total), 3)


def T(tofauti, ongezeko):
    T = (tofauti * Decimal(ongezeko)) + tofauti
    return round(Decimal(T), 3)


@csrf_exempt
def index(request):
    if request.method == 'POST':

        # Collected Data
        text = request.POST.get('text')
        phone_number = request.POST.get('phoneNumber')

        response = ""

        if text == "":
            response = "CON  Tikunet   \n"
            response += "1. Sajili \n"
            response += "2. Tuma Pesa \n"
            response += "3. Tuma Pesa 8,000 - 39,999/=\n"
            response += "4. Tuma Pesa 40,000 - 299,999/=\n"
            response += "5. Tuma Pesa 300,000 - 899,999/=\n"
            response += "6. Tuma Pesa 900,000 - 10,000,000/=\n"
            response += "00. Exit \n"

        elif text == "1":
            print(text)
            response = "CON Menu > Sajili \n"
            response += "Ingiza namba ya simu \n"

        elif text.startswith("1") and text.count("*") == 1:
            print(text)
            text_data = text.split('*')
            if len(text_data[1]) != 10:
                response = "END Namba uliyoingiza si sahihi \n"
                return HttpResponse(response)
            elif not text.startswith("1*0"):
                response = "END Namba uliyoingiza si sahihi \n"
                return HttpResponse(response)

            sajili = Sajili.objects.filter(
                phone_number=text_data[1],).exists()
            if sajili:
                response = f"END Namba ya simu imekwisha sajiliwa."
                return HttpResponse(response)

            response = "CON Ingiza Jina lako kamili \n"

        elif text.startswith("1") and text.count("*") == 2:
            print(text)
            response = "CON Ingiza Balance \n"

        elif text.startswith("1") and text.count("*") == 3:
            print(text)
            text_data = text.split('*')
            print(text_data)
            try:
                balance = int(text_data[3])
                if balance > 0:
                	response = "CON Ingiza Pin \n"
                else:
                    response = f"END Balance uliyoingiza si sahihi."
            except ValueError:
                print("That's not an int!")
                response = f"END Balance uliyoingiza si sahihi."

        elif text.startswith("1") and text.count("*") == 4:
            print(text)
            text_data = text.split('*')
            print(text_data)
            balance = int(text_data[3])

            sajili = Sajili.objects.filter(
                phone_number=text_data[1],).exists()
            if sajili:
                response = f"END Namba ya simu imekwisha sajiliwa."
                return HttpResponse(response)

            try:
                sajili = Sajili.objects.create(
                    full_name=text_data[2], phone_number=text_data[1], balance=balance, pin=text_data[4])
                if sajili:
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

            # Amount Range validation
            if 100 > amount:
                response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 100/="
            elif amount > 7999:
                response = f"END Kiasi ulichoingiza kipo juu ya Tshs. 7,999/="
            elif 100 <= amount <= 999:
                answer = calculate(amount, 8, 0.001)
                t = T(8, 0.001)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 1000 <= amount <= 1999:
                answer = calculate(amount, 275, 0.002)
                t = T(275, 0.002)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 2000 <= amount <= 2999:
                answer = calculate(amount, 295, 0.003)
                t = T(295, 0.003)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 3000 <= amount <= 3999:
                answer = calculate(amount, 375, 0.004)
                t = T(375, 0.004)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 4000 <= amount <= 4999:
                answer = calculate(amount, 400, 0.005)
                t = T(650, 0.005)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 5000 <= amount <= 5999:
                answer = calculate(amount, 550, 0.006)
                t = T(550, 0.006)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 6000 <= amount <= 7999:
                answer = calculate(amount, 680, 0.007)
                t = T(680, 0.007)
                try:
                    obj = TumaPesa.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

        elif text.startswith("2*"):
            response = "END Namba uliyoingiza si sahihi \n"

        elif text == "3":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"

        elif text.startswith("3*0") and len(text) == 12:
            response = "CON Ingiza kiasi \n"

        elif text.startswith("3*0") and text.count("*") == 2:
            receiver = text[2:12]
            amount = re.sub("3\*.+\*", '', text)
            amount = Decimal(amount)
            print(receiver)

            # Amount Range validation
            if 8000 > amount:
                response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 8000/="
            elif amount > 39999:
                response = f"END Kiasi ulichoingiza kipo juu ya Tshs. 39,999/="
            elif 8000 <= amount <= 9999:
                answer = calculate(amount, 680, 0.008)
                t = T(680, 0.008)
                try:
                    obj = TumaPesa1.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 10000 <= amount <= 19999:
                answer = calculate(amount, 1000, 0.009)
                t = T(1000, 0.009)
                try:
                    obj = TumaPesa1.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 20000 <= amount <= 29999:
                answer = calculate(amount, 1200, 0.01)
                t = T(1200, 0.01)
                try:
                    obj = TumaPesa1.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 30000 <= amount <= 39999:
                answer = calculate(amount, 1300, 0.011)
                t = T(1300, 0.011)
                try:
                    obj = TumaPesa1.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

        elif text.startswith("3*"):
            response = "END Namba uliyoingiza si sahihi \n"

        elif text == "4":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"

        elif text.startswith("4*0") and len(text) == 12:
            response = "CON Ingiza kiasi \n"

        elif text.startswith("4*0") and text.count("*") == 2:
            receiver = text[2:12]
            amount = re.sub("4\*.+\*", '', text)
            amount = Decimal(amount)
            print(receiver)

            # Amount Range validation
            if 40000 > amount:
                response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 40,000/="
            elif amount > 299999:
                response = f"END Kiasi ulichoingiza kipo juu ya Tshs. 299,999/="
            elif 40000 <= amount <= 49999:
                answer = calculate(amount, 1500, 0.012)
                t = T(1500, 0.012)
                try:
                    obj = TumaPesa2.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 50000 <= amount <= 99999:
                answer = calculate(amount, 1800, 0.013)
                t = T(1800, 0.013)
                try:
                    obj = TumaPesa2.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 100000 <= amount <= 199999:
                answer = calculate(amount, 2200, 0.014)
                t = T(2200, 0.014)
                try:
                    obj = TumaPesa2.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 200000 <= amount <= 299999:
                answer = calculate(amount, 3300, 0.015)
                t = T(3300, 0.015)
                try:
                    obj = TumaPesa2.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

        elif text.startswith("4*"):
            response = "END Namba uliyoingiza si sahihi \n"

        elif text == "5":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"

        elif text.startswith("5*0") and len(text) == 12:
            response = "CON Ingiza kiasi \n"

        elif text.startswith("5*0") and text.count("*") == 2:
            receiver = text[2:12]
            amount = re.sub("5\*.+\*", '', text)
            amount = Decimal(amount)
            print(receiver)

            # Amount Range validation
            if 300000 > amount:
                response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 300,000/="
            elif amount > 899999:
                response = f"END Kiasi ulichoingiza kipo juu ya Tshs. 899,999/="
            elif 300000 <= amount <= 399999:
                answer = calculate(amount, 4300, 0.016)
                t = T(4300, 0.016)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 400000 <= amount <= 499999:
                answer = calculate(amount, 5300, 0.017)
                t = T(5300, 0.017)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 500000 <= amount <= 599999:
                answer = calculate(amount, 5600, 0.018)
                t = T(5600, 0.018)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 600000 <= amount <= 699999:
                answer = calculate(amount, 6000, 0.019)
                t = T(6000, 0.019)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 700000 <= amount <= 799999:
                answer = calculate(amount, 6100, 0.02)
                t = T(6100, 0.02)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"
            elif 800000 <= amount <= 899999:
                answer = calculate(amount, 6350, 0.021)
                t = T(6350, 0.021)
                try:
                    obj = TumaPesa3.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

        elif text.startswith("5*"):
            response = "END Namba uliyoingiza si sahihi \n"

        elif text == "6":
            response = "CON Menu > Tuma Pesa \n"
            response += "Ingiza namba ya mpokeaji \n"

        elif text.startswith("6*0") and len(text) == 12:
            response = "CON Ingiza kiasi \n"

        elif text.startswith("6*0") and text.count("*") == 2:
            receiver = text[2:12]
            amount = re.sub("6\*.+\*", '', text)
            amount = Decimal(amount)
            print(receiver)

            # Amount Range validation
            if 900000 > amount:
                response = f"END Kiasi ulichoingiza kipo chini ya Tshs. 900,000/="
            elif amount > 10000000:
                response = f"END Kiasi ulichoingiza kipo juu ya Tshs. 10,000,000/="
            elif 900000 <= amount <= 1000000:
                answer = calculate(amount, 6500, 0.022)
                t = T(6500, 0.022)
                try:
                    obj = TumaPesa4.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 1000001 <= amount <= 3000000:
                answer = calculate(amount, 6800, 0.023)
                t = T(6800, 0.023)
                try:
                    obj = TumaPesa4.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

            elif 3000001 <= amount <= 10000000:
                answer = calculate(amount, 7000, 0.024)
                t = T(7000, 0.024)
                try:
                    obj = TumaPesa4.objects.create(
                        no_mtumaji=phone_number, no_mpokeaji=receiver, kiasi=amount, tofauti=t, jumla=answer)
                    response = f"END Umefanikiwa kutuma kiasi {amount} kwa {receiver}"
                except Exception as err:
                    print(err)
                    response = f"END Samahani kuna shida ya kimtandao {amount} kwa {receiver}"

        elif text.startswith("6*"):
            response = "END Namba uliyoingiza si sahihi \n"

        else:
            response = "END Chaguo lako sio sahihi."

        return HttpResponse(response)
