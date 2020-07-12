from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request):
    if request.method == "POST":
        title = request.post.copy()
    return render(request, "encyclopedia/get.html", {
        "data": util.get_entry(title)
    })
