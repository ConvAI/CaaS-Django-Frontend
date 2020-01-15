from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'userpanel'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.panel,name='panel'),
]