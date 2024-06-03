from django.urls import path
from . import views
from .views import ToyListView, ToyCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches_index'),
    path('finches/<int:finch_id>', views.finches_detail, name='finches_detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/edit/', views.FinchUpdate.as_view(), name='finches_edit'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('toys/', ToyListView.as_view(), name='toy_list'),
    path('toys/create/', ToyCreateView.as_view(), name='toy_create'),
    path('finches/<int:finch_id>/add_toy/', views.add_toy_to_finch, name='add_toy_to_finch'),
]