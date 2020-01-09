from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'user'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('special/',views.special,name='special'),
    path('logout/',views.user_logout,name='logout'),
]