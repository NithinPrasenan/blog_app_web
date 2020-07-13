from django.shortcuts import render


posts = [
    {
        'author': 'nithin',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '14-july-2020'
    },
    {
        'author': 'meera',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '14-july-2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')