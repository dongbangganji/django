import random

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

topics = [
    {'id': 1, 'title': 'routing1', 'body': 'dddd1'},
    {'id': 2, 'title': 'routing2', 'body': 'dddd2'},
    {'id': 3, 'title': 'routing3', 'body': 'dddd3'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
        <body>
            <h1><a href="/">Django22</a></h1>
            <ul>
                {ol}
            </ul>
            {articleTag}
            <ul>
                <a href="/create">create</a>
            </ul>
        </body>
    </html
    '''

# Create your views here.
def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))
def index2(request):
    return HttpResponse('<h1>Random</h1>'+str(random.random()))

@csrf_exempt
def create(request):
    print("request", request.method)
    article = f'''{request.method}
        <form action="/create/" method="post">
            <p><input type="text" name="title"></p> 
            <p><textarea name="body"></textarea></p> 
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))