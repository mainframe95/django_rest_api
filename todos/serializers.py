from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task','doDate','isDone','createdAt','updatedAt', 'user']

        def create(self, validate_data):
            return Todo.objects.create(**validate_data)