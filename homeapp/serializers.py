from rest_framework import serializers
from .models import AddBook

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBook
        fields = '__all__'
