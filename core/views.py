from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.models import Course
from core.models import Professor

# Create your views here.

def index(request):
	text = 'LEMME TAKE A SELFIE'
	num = 10
	template = loader.get_template('core/index.html')
	context = RequestContext(request, {
		'text' : text,
	})
	return HttpResponse(template.render(context))

def addCourseForm(request):
	context = {}
	return render(request, 'core/addcoursetemplate.html', context)

def addCourse(request):
	# Retrieve the course data input by the user
	courseId = request.POST['course_id']
	courseName = request.POST['course']
	subject = request.POST['subject']
	prof = (request.POST['firstname'], request.POST['lastname'])

	# Add the new course to the database
	newCourse = Course(courseID=courseId, name=courseName, subject=subject)
	newCourse.save()

	# see if the input prof exists, if not then create it
	try:
		profs = Professor.objects.get(first_name=prof[0], last_name=prof[1])
	except:
		newProf = Professor(first_name=prof[0],last_name=prof[1],subject=subject)
		newProf.save()
		newProf.addCourse(newCourse)
		newProf.save()

	return HttpResponseRedirect('/viewcourse/'+courseId)

def viewCourse(request, course_id):
	return HttpResponse('making sure the regex works')	
