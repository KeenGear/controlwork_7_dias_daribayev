from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Book
from .forms import BookForm


def book_list(request):
    search_post = request.GET.get('search')
    if search_post:
        guest = Book.objects.filter(Q(author=search_post))
    else:
        guest = Book.objects.filter(Q(status='Active'))
    return render(request, 'book_list.html', {'books': guest})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'
