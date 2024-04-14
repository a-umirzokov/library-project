from django.urls import path

from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    BookListApiView,
    BookCreateApiView,
    BookDeleteApiView,
    BookUpdateApiView
)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
    path('books/api/', BookListApiView.as_view(), name='book-list-api'),
    path('books/create/', BookCreateApiView.as_view(), name='book-create-api'),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book-delete-api'),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book-update-api'),
]
