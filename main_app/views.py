from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import FeedingForm, ToyForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView
from .models import Finch, Toy

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
    finch = get_object_or_404(Finch, id=finch_id)
    feedings = finch.feeding_set.all()
    form = FeedingForm()

    if request.method == 'POST':
        form = FeedingForm(request.POST)
        if form.is_valid():
            new_feeding = form.save(commit=False)
            new_feeding.finch = finch
            new_feeding.save()
            return redirect('finches_detail', finch_id=finch_id)

    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feedings': feedings,
        'form': form,
    })

def add_toy_to_finch(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    if request.method == 'POST':
        form = ToyForm(request.POST)
        if form.is_valid():
            toy = form.save(commit=False)
            toy.save()
            finch.toys.add(toy)
            return redirect('finches_detail', finch_id=finch_id)
    else:
        form = ToyForm()
    return render(request, 'finches/add_toy_to_finch.html', {'form': form})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

    def get_success_url(self):
        # Redirect to the detail view of the newly created Finch object
        return reverse_lazy('finches_detail', kwargs={'finch_id': self.object.pk})

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']
    template_name = 'main_app/finch_form.html'

class FinchDelete(DeleteView):
    model = Finch

    def get_success_url(self):
        return reverse_lazy('finches_index')
    
class ToyListView(ListView):
    model = Toy
    template_name = 'toy_list.html'

class ToyCreateView(CreateView):
    model = Toy
    fields = ['name']
    success_url = reverse_lazy('toy_list')