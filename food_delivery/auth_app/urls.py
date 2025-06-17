from django.urls import path

from auth_app.views import RegistrationView, LoginView, LogoutView, index

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]