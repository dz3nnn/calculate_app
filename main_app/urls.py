from django.urls import path

from . import views

urlpatterns = [
    path('setup_rests/', views.setup_rests, name='setup_rests'),
    path('test/', views.test, name='test')
]
