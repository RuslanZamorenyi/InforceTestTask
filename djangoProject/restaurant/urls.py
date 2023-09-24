"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from restaurant.views import RestaurantCreate, RestaurantDetail, RestaurantMenuListCreate, RestaurantMenuDetail, \
    EmployeeCreateView, EmployeeDetailView, CurrentDayMenuView, Vote, CurrentDayResultsView

urlpatterns = [
    path('restaurants/create/', RestaurantCreate.as_view(), name='restaurant-create'),
    path('restaurants/detail/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-delete'),
    path('menus/', RestaurantMenuListCreate.as_view(), name='restaurant-list-create'),
    path('menus/<int:pk>/', RestaurantMenuDetail.as_view(), name='restaurant-detail'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('restaurant/current-day/', CurrentDayMenuView.as_view(), name='current-day-restaurant'),
    path('restaurant/vote/', Vote.as_view(), name='vote'),
    path('results/current-day/', CurrentDayResultsView.as_view(), name='current-day-results'),
]