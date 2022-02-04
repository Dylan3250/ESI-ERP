from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse 👈 old
from .models import Developer


def index(request):
    # return HttpResponse("Hello, world. You're at the developers index.")
    context = {
        'developers': Developer.objects.all()
    }
    return render(request, 'developer/index.html', context)


def detail(request, developer_id):
    # developer = Developer.objects.get(pk=developer_id)
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})
