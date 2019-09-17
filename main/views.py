from django.shortcuts import render
from .models import Article

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