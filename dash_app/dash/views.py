from django.shortcuts import render


posts = [
    {
        'author': 'scd',
        'title': 'dash post 1',
        'content': 'First post content',
        'date_posted': 'jul 22, 2022'
    },
    {
        'author': 'scd1',
        'title': 'dash post 2',
        'content': 'Sec post content',
        'date_posted': 'jul 23, 2022'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'dash/home.html', context)

def services(request):
    return render(request, 'dash/services.html', {'title':'Services'})
