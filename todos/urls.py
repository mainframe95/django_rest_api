from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     # path('', TodoViewSet.as_view()),
#     path('<int:pk>/', TodoViewSet.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

app_name = "todos"
urlpatterns = [
    path('', TodoViewSet.as_view()),
    # path('<int:pk>/', TodoViewSet.as_view()),
]

# router = DefaultRouter()
# router.register('todos', TodoViewSet, 'todo')

# urlpatterns = [
#     path('all', include(router.urls)),
# ]