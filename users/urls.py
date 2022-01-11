
from .views import RegisterView, LoginView, UserView, LogoutView

from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name="Register"),
    path('login/', LoginView.as_view(), name="Logim"),
    path('user/', UserView.as_view(), name="user"),
    path('logout/', LogoutView.as_view(), name="logOut"),
]
