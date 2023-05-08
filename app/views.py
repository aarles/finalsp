from django.shortcuts import render, redirect
from app.forms import PersonForm
from app.models import Person

# Create your views here.

def home(request):
    data = {}
    data['db'] = Person.objects.all()
    return render(request, 'index.html', data)
    
def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def edit(request, id):
    data = {}
    data['form'] = PersonForm(instance=Person.objects.get(id=id))
    return render(request, 'form.html', data)

def delete(request, id):
    Person.objects.get(id=id).delete()
    return redirect('home')