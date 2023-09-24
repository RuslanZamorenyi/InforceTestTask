from datetime import date

from rest_framework import generics

from .models import Restaurant, RestaurantMenu, Employee, VotingResult
from .serializers import RestaurantSerializer, RestaurantMenuSerializer, EmployeeSerializer, VotingResultSerializer, \
    VoteSerializer


class RestaurantCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantMenuListCreate(generics.ListCreateAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer

class RestaurantMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer


class EmployeeCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CurrentDayMenuView(generics.ListCreateAPIView):
    serializer_class = RestaurantMenuSerializer

    def get_queryset(self):
        return RestaurantMenu.objects.filter(day=date.today())


class Vote(generics.ListCreateAPIView):
    queryset = VotingResult.objects.filter(menu__day=date.today())
    serializer_class = VoteSerializer


class CurrentDayResultsView(generics.ListCreateAPIView):
    serializer_class = VotingResultSerializer

    def get_queryset(self):
        return VotingResult.objects.filter(menu__day=date.today())