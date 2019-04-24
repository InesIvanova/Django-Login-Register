from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author
# Create your views here.


class BookView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class UsersBooks(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        user_id = int(self.request.user.id)
        try:
            author = Author.objects.all().filter(user__pk=user_id)[0]
            books = Book.objects.all().filter(author=author.pk)
            return books
        except:
            return []

    #this is if you want to sent more content than just the query set
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersBooks, self).get_context_data(**kwargs)
        context['can_edit'] = True
        return context
