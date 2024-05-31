from django.shortcuts import render
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