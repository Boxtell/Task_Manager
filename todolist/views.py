from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import resolve_url
from django.contrib.auth import user_logged_in
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from .models import Task, TaskList
from .forms import NewTaskForm


def go_to_description(task_id):
    return HttpResponseRedirect(reverse('todolist:display_task_detail', kwargs={'task_id': task_id}))


def go_to_list_content(task_id):
    return HttpResponseRedirect(reverse('todolist:open_list', kwargs={'task_list_id': task_id}))


@login_required
def go_to_home(request):
    return HttpResponseRedirect(reverse('todolist:list-list'))


def go_to_admin(request):
    return HttpResponseRedirect(reverse('admin'))


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todolist:list-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todolist/task_detail.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todolist/task_delete.html'


class ListListView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = 'todolist/task_list_list.html'


class ListDetailView(LoginRequiredMixin, DetailView):
    model = TaskList
    template_name = 'todolist/task_list_detail.html'


class ListCreateView(LoginRequiredMixin, CreateView):
    model = TaskList
    fields = '__all__'
    template_name = 'todolist/task_form.html'
    success_url = reverse_lazy('todolist:list-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context


class ListEditView(LoginRequiredMixin, UpdateView):
    model = TaskList
    fields = '__all__'
    template_name = 'todolist/task_form.html'
    success_url = reverse_lazy('todolist:list-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskList
    template_name = 'todolist/task_list_delete.html'
    success_url = reverse_lazy('todolist:list-list')


# def task_manager(request, task_id=None):
#     if task_id:
#         task = Task.objects.get(pk=task_id)
#
#         form = NewTaskForm(request.POST or None,
#                            instance=task)
#         action = 'Update'
#     else:
#         form = NewTaskForm(request.POST or None)
#         action = 'Create'
#
#     if form.is_valid():
#         form.save()
#
#     return render(request=request,
#                   template_name='todolist/task_form.html',
#                   context={'form': form,
#                            'action': action})
#
#
# def delete_task(request, task_id):
#     Task.objects.get(pk=task_id).delete()
#     return HttpResponseRedirect(reverse('todolist:task_list'))
#
#
# def task_list(request):
#     tasks = Task.objects.all()
#
#     context = {'tasks': tasks}
#
#     return render(request=request,
#                   template_name='todolist/task_list.html',
#                   context=context)
#
#
# def display_list_of_task_lists(request):
#     task_lists = TaskList.objects.all()
#
#     context = {'task_lists': task_lists}
#
#     return render(request=request,
#                   template_name='todolist/task_list_tasks.html',
#                   context=context)
#
#
# def display_task_detail(request, task_id):
#     task_to_display = Task.objects.get(pk=task_id)
#
#     context = {'task': task_to_display}
#
#     return render(request=request,
#                   template_name='todolist/task_detail.html',
#                   context=context)
#
#
# def open_list(request, task_list_id):
#     list_to_open = TaskList.objects.get(pk=task_list_id)
#
#     context = {'task_list': list_to_open}
#
#     return render(request=request,
#                   template_name='todolist/task_list_content.html',
#                   context=context)
