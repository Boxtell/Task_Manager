from django.urls import path

from .views import *

app_name = 'todolist'

urlpatterns = [
    # path('task/', task_list, name='task_list'),
    # path('list/', display_list_of_task_lists, name='display_task_lists'),
    # path('list_content/<int:task_list_id>', open_list, name='go_to_list_content'),
    # path('task_desc/<int:task_id>', display_task_detail, name='go_to_description'),
    # path('delete/<int:task_id>', delete_task, name='delete'),
    # path('manage/', task_manager, name='create'),
    # path('manage/<int:task_id>', task_manager, name='update'),

    path('task/', TaskListView.as_view(), name="task_list"),
    path('task_desc/<int:pk>', TaskDetailView.as_view(), name="go_to_description"),
    path('create', TaskCreateView.as_view(), name="create"),
    path('edit/<int:pk>', TaskEditView.as_view(), name="edit"),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name="delete"),

    path('list/', ListListView.as_view(), name="list-list"),
    path('list/detail/<int:pk>', ListDetailView.as_view(), name="list-detail"),
    path('list/create', ListCreateView.as_view(), name="list-create"),
    path('list/edit/<int:pk>', ListEditView.as_view(), name="list-edit"),
    path('list/delete/<int:pk>', ListDeleteView.as_view(), name="list-delete"),
]
