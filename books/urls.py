from django.urls import path
from django.views.generic.base import View


from . import views

urlpatterns = [
    # path('', views.index, name="books.index"),
    path('', views.BookListView.as_view(), name="books.index"),
    path("<int:pk>", views.BookDetailView.as_view(), name="books.show"),
    path('<int:id>/review', views.review, name="books.review"),
]
