from django.urls import path

from catalog.views import index, AuthorListView
# from catalog.views import literary_format_list_view
from catalog.views import LiteraryFormatListView, BookListView, LiteraryFormatCreateView


# from catalog.views import book_detail_view
from catalog.views import BookDetailView, test_session_view

urlpatterns = [
    path("", index, name="index"),
    path("test-sessions/", test_session_view, name="test-session"),
    path(
        "literary-formats/",
        LiteraryFormatListView.as_view(),
        name="literary-format-list"
    ),
    path(
        "literary-format/create/",
        LiteraryFormatCreateView.as_view(),
        name="literary-format-create"
    ),

    path(
        "books/",
        BookListView.as_view(),
        name="book-list",
    ),

    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        # book_detail_view,
        name="book-detail",
    ),

    path(
        "authors/",
        AuthorListView.as_view(),
        name="author-list",
    ),

]

app_name = "catalog"
