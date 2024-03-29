from django.shortcuts import render

from articles.models import Article, Tags


def articles_list(request):
    scopes = []
    template = 'articles/news.html'
    articles = Article.objects.all()
    for article in articles:
        article_dict = {'article':article, 'tags': ''}
        tag_list = []
        all_tags = article.tags.all()
        for tag in all_tags:
            tag_dict =  {'name': tag.section.name, 'main': tag.main}
            tag_list.append(tag_dict)
        tag_list = sorted(tag_list, key=lambda k: k['main'], reverse=True)
        article_dict['tags'] = tag_list
        scopes.append(article_dict)
    print(scopes)

    context = {'object_list': scopes}

    return render(request, template, context)