import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import chatbot
def home(request):
    if request.method == 'POST':
        # Handle user input
        # query = request.POST.get('query','')
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        query = data.get('query','')

        # Query the chatbot backend

        response = chatbot.get_output(query)

        # Return the chatbot response
        return JsonResponse({'response': response})
    return render(request,'myportfolioapp/portfolio.html')
