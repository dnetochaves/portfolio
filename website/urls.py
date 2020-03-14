from django.urls import path
from .views import start, contact

urlpatterns = [
    path('start/', start, name='start'),
    path('contact/', contact, name='contact'),
]
