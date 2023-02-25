from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    task = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'
