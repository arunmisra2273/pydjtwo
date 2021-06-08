from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, detail
from books.models import Book, Review

# Create your views here.

class BookListView(ListView):

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(DetailView):

    model = Book

def review(request, id):
    body = request.POST['review']
    newReview = Review(body=body, book_id=id)
    newReview.save()
    return redirect('/books')