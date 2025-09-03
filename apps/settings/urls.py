from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.settings.views import BookApiList,BookApi,AuthorApiList,AuthorApi,BookingViewSet,BorrowingViewSet,BookViewSet


router = DefaultRouter()

router.register(r'book-list', BookApiList, basename='book-list')
router.register(r'book', BookApi, basename='book')
router.register(r'author-list', AuthorApiList, basename='author-list')
router.register(r'author', AuthorApi, basename='author')
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'borrowing', BorrowingViewSet, basename='borrowing')
router.register(r"books", BookViewSet, basename="book-lists")

urlpatterns = []
urlpatterns += router.urls



