from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext

from .models import Article, images
from .forms import DocumentForm
from mysite.settings import BASE_DIR
from django.db.models import ImageField
# Create your views here.

def index(request):
	title_list = Article.objects.filter(atribute = "club")
	context = {
	'title_list' : title_list,
	}
	return render(request, 'club_index.html', context)

def article(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	return render(request, 'club_detail.html', {'paragraph':paragraph})

@login_required
def create(request):
	try:
		title = request.POST['title']
		text = request.POST['text']
		new_article = Article.objects.create(title = title, text = text, atribute = "club")
		new_article.save()
		return HttpResponseRedirect('/clubs')
	except:
		return render(request, 'club_create.html')

@login_required
def edit(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	try:
		title = request.POST['title']
		text = request.POST['text']
		paragraph.title = title
		paragraph.text = text

		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			paragraph.images_set.create(image = request.FILES['docfile'])

		paragraph.save()
		return HttpResponseRedirect('/clubs')
	except:
		form = DocumentForm()
		return render(request, 'club_edit.html',
		 {'paragraph':paragraph, 'form':form}
			)

@login_required
def delete(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	paragraph.delete()
	return HttpResponseRedirect('/clubs')

@login_required
def img_delete(request, article_id):
	paragraph = get_object_or_404(Article, pk = article_id)
	img = get_object_or_404(images, pk = request.POST['img.id'])
	img.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))