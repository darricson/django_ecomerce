from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.urls import reverse_lazy
from produto.forms import ProdutoModel
from django.contrib import messages
from .models import Produto


# Create your views here.
def home_page(request):
    context = Produto.objects.all()
    context = {'produtos': context}
    return render(request, 'produto/home_page.html', context)


def get_text_data(self, **kwargs):
    context = super(home_page, self).get_context_data(**kwargs)
    context = Produto.objects.order_by('?').all()
    return context



####################################################################

def new_product(request):
    if str(request.method) == 'POST':
        form = ProdutoModel(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso')
            form = ProdutoModel()
            return redirect('')
        else:
            messages.error(request, 'Erro ao cadastrar o produto')
    else:
        form = ProdutoModel()
    context = {'form': form}
    return render(request, 'produto/new_product.html', context)



