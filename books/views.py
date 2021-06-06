from django.shortcuts import render

import json

booksData = open('D:/pydjtwo/bookstore-project/books.json').read()
data = json.loads(booksData)

# Create your views here.

def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)

def show(request, id):
    singleBook = []
    for book in data:
        if book['id'] == id:
            singleBook = book
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
