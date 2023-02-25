from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


def book_list(request):
    tasks = Book.objects.all()
    return render(request, 'book_list.html', {'tasks': tasks})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return reverse_lazy('book_list')
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    task = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return reverse_lazy('book_list')
    return render(request, 'book_form.html', {'form': form})


def book_delete(request, pk):
    task = get_object_or_404(Book, pk=pk)
    task.delete()
    return reverse_lazy('book_list')
