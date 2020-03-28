from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'userpanel'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.panel,name='panel'),
    path('create/',views.createBot,name='createBot'),
    path('edit/<int:bot_id>/',views.editBot,name='editBot'),
    path('deploy/',views.deploy,name='deploy'),
    path('deploy/<int:bot_id>/',views.deployBot,name='deployBot'),
    path('disablebot/<int:bot_id>/',views.disableBot,name='disableBot'),

]