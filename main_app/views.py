from django.shortcuts import render

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
    return render(request, 'finches/index.html', {'finches': finches})