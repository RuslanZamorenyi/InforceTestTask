from rest_framework import serializers
from .models import Restaurant, RestaurantMenu, Employee, VotingResult


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class VotingResultSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    menu = RestaurantMenuSerializer()

    class Meta:
        model = VotingResult
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = VotingResult
        fields = ['restaurant', 'vote', 'user']