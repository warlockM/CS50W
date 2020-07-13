from django.urls import path, include

from . import views

urlpatterns = [
    path("save/", views.save, name = "save"), #this route is used to save data as md file and return to index.html
    path("create/", views.create, name="create"), #this route is used to go to the form where title and description are entered for new entry.
    path("search/", views.search, name="search"), #this route is used to search for any entry in the app.
    path("", views.index, name="index") #this route is used to visit the index
]
