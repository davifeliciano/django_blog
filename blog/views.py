from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Some test data
posts = [
    {
        "author": "DaviF",
        "title": "First Blog Post",
        "content": "Lorem Ipsum",
        "date_posted": "October 17, 2022",
    },
    {
        "author": "BiaV",
        "title": "Second Blog Post",
        "content": "Lorem Ipsum",
        "date_posted": "October 18, 2022",
    },
    {
        "author": "BelaN",
        "title": "Third Blog Post",
        "content": "Lorem Ipsum",
        "date_posted": "October 19, 2022",
    },
]


def home(request: HttpRequest) -> HttpResponse:
    context = {"posts": posts, "title": "Home"}
    return render(request, "blog/home.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/about.html", {"title": "About"})
