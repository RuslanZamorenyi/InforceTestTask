import pytest
from datetime import date
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Restaurant, RestaurantMenu, Employee, VotingResult


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_restaurant():
    return Restaurant.objects.create(name='Test Restaurant')

@pytest.fixture
def sample_menu():
    return RestaurantMenu.objects.create(
        restaurant=sample_restaurant(),
        menu_item='Sample Menu Item',
        day=date.today()
    )


def test_create_restaurant(api_client):
    url = reverse('restaurant-list')
    data = {'name': 'New Restaurant'}
    response = api_client.post(url, data, format='json')

    assert Restaurant.objects.count() == 1
    assert response.data['name'] == 'New Restaurant'


def test_retrieve_menu(api_client, sample_menu):
    url = reverse('restaurantmenu-detail', args=[sample_menu.id])
    response = api_client.get(url)

    assert response.data['menu_item'] == 'Sample Menu Item'


def test_create_employee(api_client):
    url = reverse('employee-list')
    data = {'name': 'New Employee'}
    response = api_client.post(url, data, format='json')

    assert Employee.objects.count() == 1
    assert response.data['name'] == 'New Employee'