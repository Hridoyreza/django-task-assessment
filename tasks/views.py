from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import TaskForm
# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Task.objects.filter(user=user)

        # Search by title
        search_query = self.request.GET.get('search')
        if search_query:
            try:
                queryset = queryset.filter(Q(title__icontains=search_query))
                return queryset
            except Exception as e:
                print(f"Error while filtering queryset: {e}")
        print(f"Search query: {search_query}")
        print(f"Filtered queryset: {queryset}")

        # Filter by creation date
        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(created_at__date=creation_date)

        # Filter by due date
        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        # Filter by priority
        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        # Filter by completion status
        is_complete = self.request.GET.get('is_complete')
        if is_complete:
            queryset = queryset.filter(is_complete=(is_complete == 'True'))

        return queryset

        
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    fields = ['title', 'description', 'due_date', 'priority', 'is_complete', 'img']
    success_url = reverse_lazy('task-list')
   

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        # Get the current user
        current_user = self.request.user

        # Set the user field in the form to the current user
        form.instance.user = current_user

        return super().form_valid(form)