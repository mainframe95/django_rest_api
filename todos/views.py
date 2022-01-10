
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
# from rest_framework import viewsets
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-detail/<str:pk>/',
        'List': '/task-list',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    print('task \n', tasks)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id = pk)
    print('task \n', tasks)
    serializer = TaskSerializer(tasks, many = False)
    print('serializer.data \n', serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
        
    return Response("Deleted success")