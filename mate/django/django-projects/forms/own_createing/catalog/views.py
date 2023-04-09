from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import AuthorCreationForm, AuthorUpdateForm, BookForm, BookSearchForm
from catalog.models import Book, Author, LiteraryFormat


PAGINATION_LIMIT = 2


@login_required
def index(request: HttpRequest):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
    }

    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    # paginate_by = PAGINATION_LIMIT


class LiteraryFormatDetailView(LoginRequiredMixin, generic.DetailView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_detail.html"


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    template_name = "catalog/literary_format_form.html"
    success_url = reverse_lazy("catalog:literary-format-list")


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    template_name = "catalog/literary_format_form.html"
    success_url = reverse_lazy("catalog:literary-format-list")


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_confirm_delete.html"
    success_url = reverse_lazy("catalog:literary-format-list")


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    # queryset = Book.objects.select_related("format")  - if not overwriting get_queryset method
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")  # чтобы не стиралось в поле поиска, записываем в BookSearchForm ниже

        context["search_form"] = BookSearchForm(initial={"title": title})

        return context

    def get_queryset(self):
        # queryset = Book.objects.select_related("format")
        queryset = Book.objects.all()

        form = BookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])

        return queryset


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("catalog:book-list")


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    # model = Book
    # fields = "__all__"
    form_class = BookForm
    success_url = reverse_lazy("catalog:book-list")


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy("catalog:book-list")


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm
    success_url = reverse_lazy("catalog:author-list")


class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    # fields = "__all__"
    form_class = AuthorUpdateForm  # or it
    success_url = reverse_lazy("catalog:author-list")


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy("catalog:author-list")

