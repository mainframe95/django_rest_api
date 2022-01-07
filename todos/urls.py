from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet, 'todo')

urlpatterns = [
    path('all', include(router.urls)),
]