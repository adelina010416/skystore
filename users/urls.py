from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile_edit/', EditProfileView.as_view(), name='profile_edit'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login-fail/', login_fail, name='login_fail'),
    path('verifying/', verify_view, name='verifying'),
    path('confirm-mail/', confirm_mail, name='confirm_mail'),
    path('reset_done/', UserPasswordResetDoneView.as_view(), name='reset_done'),
    path('recover-password/', UserPasswordResetView.as_view(), name='recover_password'),
    path('wrong-mail/', wrong_mail, name='wrong_mail'),
]
