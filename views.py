import requests
from django.shortcuts import render

def index(request):
 
response1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
data1 = response1.json()
fact1 = data1['fact']

response2 = requests.get('https://freetestapi.com/api/v1/joke')
data2 = response2.json()
fact2 = data2['fact']

response3 = requests.get('https://freetestapi.com/api/v1/joke')
data3 = response3.json()
fact3 = data2['image']

return render(request, 'templates/index.html', {'fact':fact})