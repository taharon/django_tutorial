from django.urls import path

from . import views

urlpatterns = [
  # so this path already has /polls/ from the tutorial_project urls.py. The views.index tells it to go to views
  #   and take the index function I guess. not sure why I need hte name = index part
  # from tutorial, path gets 4 arguments: route, view, [kwargs, name]
  # route: the url pattern. I don't think this knows the difference between say a GET and a POST
  # view: once django finds a matching pattern, it calls the specified view using the HttpRequest Object, and
  #   any arguments from your URI as kwargs
  # [kwargs] optional, a dictionary of arguments passed to the view
  # [name]  optional, lets you name your view, which apparently lets you refer to it elsewhere
  path('', views.index, name='index'),

]