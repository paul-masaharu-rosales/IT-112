from django.urls import path
from django_assignment import views
from .views import FruitCreate, FruitListAll, FruitRetrive



urlpatterns = [
    path('fruit/create/', FruitCreate.as_view(), name='Fruit Create'), #adds new fruit
    path('fruit/listAll/', FruitListAll.as_view(), name='Fruit List All'), #returns all fruit and returns in json format
    path('fruit/<int:pk>/',FruitRetrive.as_view(), name='Single Fruit Details'), #returns all fruit based on id
]