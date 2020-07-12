from django.shortcuts import render
from django.http import HttpResponse

from . import util

title = ""

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == "POST":
        title = request.POST.get("q")
    else:
        return HttpResponse("Resubmit form!")
    return render(request, "encyclopedia/get.html", {
        "data": util.get_entry(title), "header": title
    })
