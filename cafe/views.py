from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#PAGINA PRINCIPAL DO SITE
def home(request):
    return render(request, 'index.html')