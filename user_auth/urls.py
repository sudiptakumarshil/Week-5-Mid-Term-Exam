from django.urls import path
from .views import *

urlpatterns = [
    path('user/login',user_login,name='user.login'),
    path('user/logout',user_logout,name='user.logout'),
    path('user/register',user_register,name='user.register'),
    path('user/profile',user_profile,name='user.profile'),
    path('user/change-password',password_change,name='user.password_change'),
    path('user/change-password-except-old',password_change_except_old,name='user.password_change_except_old'),
    path('user/update-profile',changeUserProfile,name='user.update_profile')
]