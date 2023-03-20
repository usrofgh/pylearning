import datetime

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Book, Author, LiteraryFormat


# def hello_world(request, unique_number: int):
#     print("REQUEST METHOD: ", request)
#     print("Unique number: ", unique_number)
#     print("Request GET: ", request.GET)
#     now = datetime.datetime.now()
#     return HttpResponse()


def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    user = request.user
    par = request.GET

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
        "user": user,
        "params": par,
    }

    return render(request, "catalog/index.html", context=context)
