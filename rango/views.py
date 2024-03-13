from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse(
        "<h1>Rango says here is the about page.</h1>"
        "<a href='/rango/'>Index</a>"
    )
