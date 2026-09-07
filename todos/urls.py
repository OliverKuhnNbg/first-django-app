from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_py_view, name='hello_python'),
    path('hello', views.hello_world_view, name='hello_world'),
    path('hellohtml', views.hello_html_view, name='hello_html'),
    path('helloredirect', views.special_view, name='hello_redirect'),
    path('helloname/<str:name>', views.hello_path_view, name='hello_path'),
    path('add/<int:num1>/<int:num2>', views.happy_sum_view, name='happy_sum'),
    path('search', views.search_query_view, name='search_query'),
    path('postapi', views.post_example, name='post_api'),
    path('submitapi', views.submit_example, name='submit_api'),
    path('postformapi', views.post_form_example, name='post_form_api'),
    path('submitformapi', views.submit_form_example, name='submit_form_api'),
    path('template', views.template_view, name='template_view'),
    path('todos', views.todos_view, name='todos_view'),
]