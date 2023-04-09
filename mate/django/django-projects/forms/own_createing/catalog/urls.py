from django.urls import path

from catalog.views import (
    index,
    LiteraryFormatListView, LiteraryFormatDetailView, LiteraryFormatCreateView, LiteraryFormatUpdateView,
    LiteraryFormatDeleteView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path("", index, name="index"),

    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("literary-formats/<int:pk>/", LiteraryFormatDetailView.as_view(), name="literary-format-detail"),
    path("literary-formats/create/", LiteraryFormatCreateView.as_view(), name="literary-format-create"),
    path("literary-formats/<int:pk>/update/", LiteraryFormatUpdateView.as_view(), name="literary-format-update"),
    path("literary-formats/<int:pk>/delete/", LiteraryFormatDeleteView.as_view(), name="literary-format-delete"),


    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),


    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]

app_name = "catalog"
