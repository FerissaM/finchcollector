from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Finch

# Create your views here.
finches = [
    {'name': 'House Finch', 'species': 'Haemorhous mexicanus', 'description': 'Small-bodied bird', 'age': 2},
    {'name': 'American Goldfinch', 'species': 'Spinus tristis', 'description': 'Bright yellow color', 'age': 3},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = reverse_lazy('finches_index')

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']
    success_url = reverse_lazy('finches_index')

class FinchDelete(DeleteView):
    model = Finch
    success_url = reverse_lazy('finches_index')