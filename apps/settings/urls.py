from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.settings.views import BookApiList,BookApi,AuthorApiList,AuthorApi


router = DefaultRouter()

router.register(r'book-list', BookApiList, basename='book-list')
router.register(r'book', BookApi, basename='book')
router.register(r'author-list', AuthorApiList, basename='author-list')
router.register(r'author', AuthorApi, basename='author')

urlpatterns = [

]


urlpatterns += router.urls



# from apps.settings.views import (
#     BookRetrieveAPIView,LibraryAPIView, BookAPIView, AuthorAPIView, 
#     BookCreateAPIView,BookDetailAPIView,BookUpdateAPIView,BookDeleteAPIView,
#     AuthorCreateAPIView,AuthorDeleteAPIView,AuthorRetrieveAPIView,AuthorUpdateAPIView)
# urlpatterns = [
#     path("book-update/<int:pk>/", BookUpdateAPIView.as_view(), name='update-book'),
#     path("list-library/", LibraryAPIView.as_view(), name='list-library'),
#     path("books-list/", BookAPIView.as_view(), name='list-books'),
#     path("authors-list/", AuthorAPIView.as_view(), name='list-authors'),

#     path("book-delete/<int:pk>/", BookDeleteAPIView.as_view(), name='delete-book'),
#     path("book-retrieve/<int:pk>/", BookRetrieveAPIView.as_view(), name='retrieve-book'),
#     path("book-detail/<int:pk>/", BookDetailAPIView.as_view(), name='book-detail'),
#     path("create-book/", BookCreateAPIView.as_view(), name='create-book'),
#     path("create-author/", AuthorCreateAPIView.as_view(), name='create-author'),
#     path("author-retrieve/<int:pk>/", AuthorRetrieveAPIView.as_view(), name='retrieve-author'),
#     path("author-update/<int:pk>/", AuthorUpdateAPIView.as_view(), name='update-author'),
#     path("author-delete/<int:pk>/", AuthorDeleteAPIView.as_view(), name='delete-author'),
#     path('')
# ]
