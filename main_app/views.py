from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

    return render(request, 'finches/detail.html', {'finch': finch, 'feedings': feedings, 'form': form})

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