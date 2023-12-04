from django.shortcuts import render, redirect
from .models import transacao
from .forms import TransacaoForm 
import datetime


def home(request):
    data = {}
    data['transações'] = ['T1', 'T2', 'T3']   

    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, "contas/home.html", data)

def listagem(request):
    data = {}
    data['transações'] = transacao.objects.all()
    return render(request, "contas/listagem.html", data)

def form(request):
    data = {}
    form = TransacaoForm(request.POST or None)  
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')  
    
    data['form'] = form
    return render(request, "contas/form.html", data)

def update(request, pk):
    data = {}
    ttransacao = transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=ttransacao)
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    data['form'] = form
    data['transacao'] = ttransacao
    return render(request, "contas/form.html", data)

def delete(request, pk):
    ttransacao = transacao.objects.get(pk=pk)
    ttransacao.delete()
    return redirect('url_listagem')
    
