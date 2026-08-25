from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', {})

def listanumeros(n1):
    for n1 in range(1, 100):
        print(n1)