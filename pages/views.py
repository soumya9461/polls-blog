from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def post_list(request):
    return render(request, 'pages/index.html')
