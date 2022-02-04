from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import DeveloperForm
from .models import Developer


class IndexView(ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = DeveloperForm
        return context


def index(request):
    # return HttpResponse("Hello, world. You're at the developers index.")
    context = {
        'developers': Developer.objects.all(),
        'form': DeveloperForm
    }
    return render(request, 'developer/index.html', context)


class DevDetailVue(DetailView):
    model = Developer
    template_name = 'developer/detail.html'


# def detail(request, developer_id):
#     # developer = Developer.objects.get(pk=developer_id)
#     developer = get_object_or_404(Developer, pk=developer_id)
#     return render(request, 'developer/detail.html', {'developer': developer})


def create(request):
    form = DeveloperForm(request.POST)
    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))
