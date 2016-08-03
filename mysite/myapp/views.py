from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm
# Create your views here.
def list(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newimg = Document(docfile = request.FILES['docfile'])
			newimg.save()

			return HttpResponseRedirect('/myapp')
	else:
		form = DocumentForm()

	documents = Document.objects.all()

	return render_to_response(
		'myapp/list.html',
		{'documents': documents, 'form':form},
		context_instance = RequestContext(request)
		)

def index(request):
	return render_to_response('myapp/index.html')