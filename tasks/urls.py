from django.urls import path
from .views import *

urlpatterns=[
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]