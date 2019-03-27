from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='Blog-home'),
     path('about/',views.about,name='About-Blog'),
     path('cart/',views.about,name='Cart'),

]
