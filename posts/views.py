"""Post views."""

#Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts =[
        {
            'name': 'Mont Blac',
            'user': 'Yésica Cortés',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE',
        },
        {
            'name': 'Via Láctea',
            'user': 'C. Vander',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://i.picsum.photos/id/903/200/200.jpg?hmac=lxHKyjlQqAkKyuVGkgUCO_jdWkg3osj3nTuULFHZxH8',
        },
        {
            'name': 'Nuevo auditorio',
            'user': 'Thespianartist',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://i.picsum.photos/id/1076/200/200.jpg?hmac=KTOq4o7b6rXzwd8kYN0nWrPIeKI97mzxBdWhnn-o-Nc',
        },
    ]

def list_posts(request):
    """List existing posts."""
    content=[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))