from django.urls import path
from .views import RatingList, RatingDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('ratings/<int:pk>/', RatingDetail.as_view()),
    path('ratings/', RatingList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('categories/', CategoryList.as_view()),
]