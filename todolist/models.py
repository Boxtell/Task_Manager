from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    list_title = models.CharField(max_length=100,
                                  verbose_name="List Title",
                                  null=False,
                                  blank=False,
                                  editable=True)
    list_users = models.ManyToManyField(to=User,
                                        related_name='lists')

    def __str__(self):
        return self.list_title


class Task(models.Model):
    task_name = models.CharField(max_length=200,
                                 verbose_name="Task Name",
                                 null=False,
                                 blank=False,
                                 editable=True)

    task_description = models.TextField(verbose_name="Task Description",
                                        default="Ajouter une description")

    task_due_date = models.DateField(verbose_name="Task Deadline")
    task_time = models.DurationField(verbose_name="Task Duration")

    task_ended = models.BooleanField(verbose_name="Is Done ?",
                                     default=False)

    task_priority = models.IntegerField(verbose_name="Priority",
                                        choices=((1, "High"), (2, "Medium"), (3, "Low"),),
                                        default=3)
    task_list = models.ForeignKey(to=TaskList,
                                  related_name='tasks',
                                  on_delete=models.SET_NULL,
                                  null=True)

    def __str__(self):
        return '{} {}'.format(self.task_name, self.task_due_date)



