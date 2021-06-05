from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'name': 'Purnima'}
    return render(request, 'books/index.html', context)