from django.urls import path
from .views import TaskCreateView, TaskRetrieveUpdateDeleteAPIView


urlpatterns = [
    path('tasks/create', TaskCreateView.as_view(), name='task_api-create'),
    path('tasks/<int:pk>', TaskRetrieveUpdateDeleteAPIView.as_view(), name='task_api-rud')
]