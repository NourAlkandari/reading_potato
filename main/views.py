from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
################--LIST_PAGE--########################

def articles_list(request):
	context = {
		"articles" : Article.objects.all(),
	}
	
	return render(request, "articles_list.html", context)

################--DETAIL_PAGE--########################

def article_details(request, article_id):
	context = { 
	"article" : Article.objects.get(id=article_id)
	}

	return render(request, 'article_details.html', context)

################--CREATE_FORM--########################

def create_article(request):
	form = ArticleForm()
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.author = request.user
			article.save()
			return redirect('article-details', article.id)

	context = {"form" : form}

	return render(request, "create_article.html", context)


################--EDIT_FORM--########################

def edit_article(request, article_id):

	article = Article.objects.get(id=article_id)

	form = ArticleForm(instance=article)

	if request.method == "POST":
		form = ArticleForm(request.POST, instance=article)

		if form.is_valid():
			form.save()
			return redirect('article-details', article_id)


	context = { "form" : form ,
	"article" : article}
	
	

	return render(request, 'edit_article.html', context)

	###########---MY_list----###################################
def my_article_list(request):
	return render(request, "my_articles_list.html")
