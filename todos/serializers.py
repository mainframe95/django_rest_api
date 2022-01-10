from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['task','doDate','isDone','createdAt','updatedAt', 'user']

        # def create(self, validate_data):
        #     return Task.objects.create(**validate_data)