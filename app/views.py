from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.forms import PergForm
from app.models import Perguntas

# Create your views here.

@login_required
def home(request):
    data = {}
    data['db'] = Perguntas.objects.all()
    return render(request, 'index.html', data)

@login_required    
def form(request):
    data = {}
    data['form'] = PergForm()
    return render(request, 'perg.html', data)

@login_required
def create(request):
    form = PergForm(request.POST or None)
    if form.is_valid():    
        form.save()
        return redirect('home')

@login_required
def delete(request, id):
    Perguntas.objects.get(id=id).delete()
    return redirect('home')

def login(request):
    return render(request, 'login.html')

@login_required    
def update_view(request, id):
       my_object = Perguntas.objects.get(id=id)
       if request.method == 'POST':
           form = PergForm(request.POST, instance=my_object)
           if form.is_valid():
               form.save()
               return redirect('home')
       else:
           form = PergForm(instance=my_object)
       return render(request, 'resp.html', {'form': form})