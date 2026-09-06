from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_py_view, name='hello_python'),
    path('hello', views.hello_world_view, name='hello_world'),
    path('hellohtml', views.hello_html_view, name='hello_html'),
]