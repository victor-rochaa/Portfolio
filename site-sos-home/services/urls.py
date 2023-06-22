from django.urls import path
from django.contrib.auth import login
from .views import ServiceList, DeleteServices, UpdateSchedule, Budget, UpdateBudget

urlpatterns = [
    path('user/<int:user_id>', ServiceList, name='services'),
    path('<int:employee_id>/delete/<int:pk>', DeleteServices.as_view(), name='services-delete'),
    path('schedule/<int:employee_id>/edit/<int:pk>', UpdateSchedule.as_view(), name='schedule-update'),
    path('budget/<int:employee_id>', Budget, name='budget'),
    path('budget/<int:employee_id>/edit/<int:pk>', UpdateBudget.as_view(), name='budget-update'),
]