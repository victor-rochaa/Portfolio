from rest_framework import serializers

from pages.models import Category
from accounts.models import Rating

        
class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'author', 'date', 'body', 'rate', 'profile']
        
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'employee_set']
        