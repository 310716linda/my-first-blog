from django.urls import path
from . import views

#Mi primera URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
]