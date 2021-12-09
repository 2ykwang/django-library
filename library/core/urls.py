from django.urls import path

from library.core.views import book_details, index

app_name = "core"

urlpatterns = [
    path("", view=index),
    path("book/", view=book_details, name="book_details"),
]
