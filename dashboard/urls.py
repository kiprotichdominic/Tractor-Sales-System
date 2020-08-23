from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('dashboard/', HomePageView.as_view(), name='dashboard'),
]