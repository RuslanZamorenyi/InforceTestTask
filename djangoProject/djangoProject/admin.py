from django.contrib import admin

from restaurant.models import Restaurant, RestaurantMenu, Employee, VotingResult


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(RestaurantMenu)
class DishAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(VotingResult)
class VotingResultAdmin(admin.ModelAdmin):
    pass