from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from core.models import Course

# Create your views here.

@login_required
def index(request):
	text = 'LEMME TAKE A SELFIE'
	num = 10
	template = loader.get_template('core/index.html')
	context = RequestContext(request, {
		'text' : text,
	})
	return HttpResponse(template.render(context))
	
