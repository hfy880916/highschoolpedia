from django.shortcuts import render, get_object_or_404
from clubs.models import Article
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	title_list = Article.objects.filter(atribute = "classes")
	context = {
	'title_list' : title_list,
	}
	return render(request, 'class_index.html', context)

def article(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	return render(request, 'class_detail.html', {'paragraph':paragraph})

@login_required
def create(request):
	try:
		title = request.POST['title']
		text = request.POST['text']
		new_article = Article.objects.create(title = title, text = text, atribute = "classes")
		new_article.save()
		return HttpResponseRedirect('/classes')
	except:
		return render(request, 'class_create.html')

@login_required
def edit(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	try:
		title = request.POST['title']
		text = request.POST['text']
		paragraph.title = title
		paragraph.text = text
		paragraph.save()
		return HttpResponseRedirect('/classes')
	except:
		return render(request, 'class_edit.html', {'paragraph':paragraph})

@login_required
def delete(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	paragraph.delete()
	return HttpResponseRedirect('/classes')