from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import action
from rest_framework import permissions
from apps.settings.models import Author, Book, Library, Booking,Borrowing
from apps.settings.serializers import (
    AuthorSerializer, BookSerializer, BookDetailSerializer, LibrarySerilizer, BookingSerializer, BorrowingSerializer
)



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'birth_year']
    ordering = ['id']
    pagination_class = StandardResultsSetPagination

class AuthorApiList(ListModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorApi(CreateModelMixin,
                RetrieveModelMixin,
                UpdateModelMixin,
                DestroyModelMixin,
                GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'library']  # фильтрация по автору и библиотеке
    search_fields = ['title']
    ordering_fields = ['title', 'published_year']
    ordering = ['id']
    pagination_class = StandardResultsSetPagination

class BookApi(CreateModelMixin,
              RetrieveModelMixin,
              UpdateModelMixin, 
              DestroyModelMixin, 
              GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookApiList(ListModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


@method_decorator(cache_page(60), name='dispatch')
class LibraryListAPIView(generics.ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerilizer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'id']
    ordering = ['id']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'book', 'is_active'] 
    ordering_fields = ['booked_at', 'return_date']
    ordering = ['booked_at']
    pagination_class = StandardResultsSetPagination

# дз 7
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# конец дз 7
class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Borrowing.objects.filter(reader__user=user)

    @action(detail=False, methods=['get'])
    def return_book(self, request):
        borrowings = self.get_queryset()
        if borrowings.returned:
            return Response({"detail" : "Книга уже возвращена"}, status=400)
        borrowings.mark_as_returned()
        return Response({"detail":"Книга успешно возвращена"})

