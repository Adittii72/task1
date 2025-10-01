from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_search_view, name='case_search'),
]