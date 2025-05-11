from django.urls import path
from .views import UserRegisterView, UserLoginView, AdminView, StaffView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('admin/', AdminView.as_view(), name='admin'),
    path('staff/', StaffView.as_view(), name='staff'),
]
