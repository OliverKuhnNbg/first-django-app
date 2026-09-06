from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

def hello_world_view(request):
    return HttpResponse("Hello World")

def hello_py_view(request):
    return HttpResponse("Hello Pyton - Start Page")

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path_view(request, name):
    return HttpResponse(f'Hello {name}!')

def happy_sum_view(request, num1, num2):
    return HttpResponse(f'Sum of {num1} & {num2} is {num1 + num2}!')

def search_query_view(request):
    return HttpResponse(f'Your query: <strong>{request.GET.get("q")}</strong>')

def special_view(request):
    # do some stuff
    return redirect('hello_html')

def post_example(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        job = request.POST.get('job')
        return HttpResponse(f'Your post: <strong>{name}, {age}, {job}</strong>')
    else:
        return HttpResponseNotAllowed(['POST'])

def submit_example(request):
        return render(request, 'todos/submit.html')