from django.shortcuts import render


def home(request):
    context = {
        'title': 'Full Stack Development Lab',
        'heading': 'Implementing Django Views and Templates',
        'name': 'Binish',
        'is_logged_in': True,
        'subjects': [
            'Python',
            'Django',
            'HTML',
            'CSS'
        ]
    }

    return render(request, 'myapp/home.html', context)