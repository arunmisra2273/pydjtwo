from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path("<int:id>", views.show, name="books.show"),
    path('review', views.review, name="books.review"),
]