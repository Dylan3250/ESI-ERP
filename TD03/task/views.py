from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .forms import TaskForm

from .models import Task


class IndexView(ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


def index(request):
    context = {
        'tasks': Task.objects.all(),
        'form': TaskForm
    }
    return render(request, 'task/index.html', context)


def delete(request, task_id):
    if request.method == "POST":
        get_object_or_404(Task, pk=task_id).delete()
        return HttpResponseRedirect(reverse('task:index'))
    return HttpResponseNotFound()


def create(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            assignee=form.cleaned_data['assignee'],
        )
    return HttpResponseRedirect(reverse('task:index'))
