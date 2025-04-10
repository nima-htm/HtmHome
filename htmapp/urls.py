from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registeration/',views.registeration,name='registeration'),
    path('dict/',views.dict,name='dict'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]