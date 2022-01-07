
from rest_framework.fields import JSONField
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Todo
# from rest_framework import viewsets
from .serializers import TodoSerializer


class TodoViewSet(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many = True)
        return Response({"todos": serializer.data})

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = TodoSerializer(snippet)
    #     return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class TodoViewSet(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()