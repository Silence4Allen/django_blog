from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = f'title:{title}, brief_content:{brief_content}, content:{content}, article_id:{article_id}, publish_date:{publish_date}'
    return HttpResponse(return_str)


def get_index_page(request):
    """
    获取blog首页
    """
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    all_article = Article.objects.all()
    top_article_list = Article.objects.order_by('-publish_date')[3:]

    # 分页
    paginator = Paginator(all_article, 5)
    page_num = paginator.num_pages

    previous_page, next_page = None, None
    page_article_list = paginator.page(page)
    if page_article_list.has_previous():
        previous_page = page - 1
    if page_article_list.has_next():
        next_page = page + 1

    return render(
        request=request,
        template_name='blog/index.html',
        context={
            'article_list': page_article_list,
            'page_num': range(1, page_num + 1),
            'cur_page': page,
            'previous_page': previous_page,
            'next_page': next_page,
            'top_article_list': top_article_list
        }
    )


def get_detail_page(request, article_id):
    """
    获取blog详情界面
    """
    article_list = Article.objects.all()
    article, previous_article, next_article = None, None, None
    for article_item in article_list:
        if article_id == article_item.article_id:
            article = article_item
            continue
        if not article:
            previous_article = article_item
        if article and not next_article:
            next_article = article_item
            break
    section_list = article.content.split('\n')
    return render(
        request=request,
        template_name='blog/detail.html',
        context={
            'article': article,
            'section_list': section_list,
            'previous_article': previous_article,
            'next_article': next_article
        }
    )
