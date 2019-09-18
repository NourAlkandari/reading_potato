from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles_list(request):

	
	context = {
		"articles" : Article.objects.all(),
	}
	
	return render(request, "articles_list.html", context)

def article_details(request, article_id):
    context = { 
    "article" : Article.objects.get(id=article_id)
    }

    return render(request, 'article_details.html', context)

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