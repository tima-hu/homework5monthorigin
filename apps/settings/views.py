from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.settings.models import Library, Author, Book
from apps.settings.serializers import (
    LibrarySerilizer, 
    BookSerializer, 
    AuthorSerializer, 
    BookDetailSerializer
)
class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'birth_year']
    ordering = ['id']

# class BookApi(CreateModelMixin,
#               RetrieveModelMixin,
#               UpdateModelMixin, 
#               DestroyModelMixin, 
#               GenericViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

# class AuthorApiList(ListModelMixin, GenericViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorApi(CreateModelMixin,
#                 RetrieveModelMixin,
#                 UpdateModelMixin,
#                 DestroyModelMixin,
#                 GenericViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# # Получение всех библиотек
# class LibraryAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         libraries = Library.objects.all()
#         serializer = LibrarySerilizer(libraries, many=True)
#         return Response(serializer.data)

# # Получение списка книг
# @method_decorator(cache_page(60), name='dispatch')
# class BookAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # Получение списка авторов
# @method_decorator(cache_page(60), name='dispatch')
# class AuthorAPIView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# # Создание книги
# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # Получение книги по pk
# class BookRetrieveAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # Детальная информация по книге по pk
# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

# class BookUpdateAPIView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

# class BookDeleteAPIView(APIView):
#     def delete(self, request, pk, *args, **kwargs):
#         try:
#             book = Book.objects.get(pk=pk)
#             book.delete()
#             return Response({"message": "Book deleted successfully"}, status=204)
#         except Book.DoesNotExist:
#             return Response({"error": "Book not found"}, status=404)


# class AuthorCreateAPIView(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorRetrieveAPIView(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorUpdateAPIView(UpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorDeleteAPIView(DestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
