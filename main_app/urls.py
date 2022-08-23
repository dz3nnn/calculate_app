from django.urls import path

from . import views

urlpatterns = [
    path('setup_rests/', views.setup_rests),
]
