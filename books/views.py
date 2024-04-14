from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"{len(serializer_data)} books found",
            'books': serializer_data
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': 'New book created',
                'book': serializer.data
            }
            return Response(data, status=201)


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            data = {
                'status': True,
                'message': 'Book deleted'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            data = {
                'status': False,
                'message': 'Book is not found'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': True,
                'message': 'Book updated',
                'book': serializer.data
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=400)
