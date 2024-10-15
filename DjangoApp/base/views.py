from django.shortcuts import render
from base.data import articles
import random, time

def index(request):
    return render(request, "base/index.html", 
        {
            'title': "SPA HTMX Example Project",
            'articles': articles.articles
    })

def article_detail(request, id):
    # Find Article
    data = articles.articles
    obj = next(obj for obj in data if obj["id"] == id)

    return render(request, "base/article_detail.html", 
        {
            'title': obj['name'],
            'article': obj
    })

def articles_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        body = request.POST.get("body")

        data = articles.articles
        
        data.append(
            {'id': random.randint(1,10000000), 'name': name, 'body': body}
        )

        time.sleep(3)

        return render(request, "base/partials/list.html", {'articles': data })