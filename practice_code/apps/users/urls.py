from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.users.views import RegisterView, LoginView, ProfileView, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<str:token>/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]

