from django.contrib.auth import views as auth_views
from django.urls import path
from .views import RegisterView, LoginView, logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', logout, name='logout_page'),
]
