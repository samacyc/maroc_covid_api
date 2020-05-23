from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
from django.http import JsonResponse


def homepage(request):

    page = requests.get(
        'https://covid.hespress.com/')
    page.encoding = "utf-8"

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.findAll("div", {"class": "col-7 text-left"})
    table = soup.findAll('tr')
    general = []
    states = []

    for row in rows:
        data = {
            'title': row.h5.getText(),
            'value': row.h4.getText()
        }
        general.append(data)
    for tab in table:
        td = tab.findAll('td')
        print(td)
        data = {
            'state': tab.th.a.getText(),
            'total': td[0].getText(),
            'new_cases': td[1].getText()

        }
        states.append(data)
    responseData = {
        'general': general,
        'states': states
    }

    return JsonResponse(responseData)
