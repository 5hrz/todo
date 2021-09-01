from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items, name='app'),
    path('register/', views.register_user, name='app')
]
