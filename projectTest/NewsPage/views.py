from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArticleForm

import datetime


def article_list(request):
    articles = Article.objects.filter(current_status=Article.PUBLISH).order_by('-created_at')
    return render(request, 'NewsPage/article_list.html', {'articles': articles})


def article_draft_list(request):
    articles = Article.objects.filter(current_status=Article.DRAFT).order_by('-created_at')
    return render(request, 'NewsPage/article_draft_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'NewsPage/article_detail.html', {'article': article})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()

    return render(request, 'NewsPage/article_edit.html', {'form': form})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'NewsPage/article_edit.html', {'form': form})
