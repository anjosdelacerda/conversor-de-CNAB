from django.urls import path

from .views import ConversorCNAB

urlpatterns = [
    path('file/', ConversorCNAB.as_view()),
]
