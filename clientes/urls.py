from django.urls import path

from .views import ConversorCNAB

urlpatterns = [
    path('', ConversorCNAB.as_view()),
]
