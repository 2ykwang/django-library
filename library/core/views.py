from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("안녕하세요")


def book_details(request):
    return render(request, "core/book_details.html", {"test": "hello world"})
