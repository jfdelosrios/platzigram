"""Post views."""

#Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts =[
        {
            'title': 'Mont Blanc',
            'user': {
                'name':'Yésica Cortés',
                'picture': 'https://picsum.photos/60/60/?image=1027',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE',
        },
        {
            'title': 'Via Láctea',
            'user': {
                'name':'Christian Vander Henst',
                'picture':'https://picsum.photos/60/60/?image=1005',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://i.picsum.photos/id/903/200/200.jpg?hmac=lxHKyjlQqAkKyuVGkgUCO_jdWkg3osj3nTuULFHZxH8',
        },
        {
            'title': 'Nuevo auditorio',
            'user': {
                'name':'Uriel (thepianastist)',
                'picture':'https://picsum.photos/60/60/?image=883',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://i.picsum.photos/id/1076/200/200.jpg?hmac=KTOq4o7b6rXzwd8kYN0nWrPIeKI97mzxBdWhnn-o-Nc',
        },
    ]

def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})