import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, LiteraryFormat


@login_required
def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    user = request.user
    par = request.GET

    # Якщо в session є num_visits - повертає та ітерує, якщо ні - створюеє
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
        "user": user,
        "params": par,
        "num_visits": request.session["num_visits"]
    }

    return render(request, "catalog/index.html", context=context)

# # function approach
# def literary_format_list_view(request):
#     literary_format_list = LiteraryFormat.objects.all()
#
#     context = {
#         "literary_format_list": literary_format_list_view
#     }
#
#     # someone use literary_format merged
#     return render(request, "catalog/literary_format_list.html", context)


# class approach
class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    # django by default unions these two words to literaryformat_list.
    # But we have literary_format_list. add template_name, also change in html - context-object-name
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.all().select_related("format")
    paginate_by = 10  # ?page=1


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author



# def book_detail_view(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Http404("Book does not exist")
#     context = {
#         "book": book,
#     }
#
#     return render(request, "catalog/book_detail.html", context)


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book




def test_session_view(request):
    # request.session["book"] = "Test session book"

    # session = Session.objects.get(session_key="")
    # session.get_decoded()

    return HttpResponse(
        "<h1>Test Session</h1>"
        f"<h4>Session data: {request.session['book']}</h4>"
    )