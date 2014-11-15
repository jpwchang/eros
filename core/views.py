from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from core.models import Course
from core.models import Professor
from core.models import Review

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

	# check to see if course already exists. If so, redirect to it
	try:
		theCourse = Course.objects.get(courseID=courseId)
		return HttpResponseRedirect('/viewcourse/'+courseId)
	except:
		# Add the new course to the database
		newCourse = Course(courseID=courseId, name=courseName, subject=subject)
		newCourse.save()
	
		# see if the input prof exists, if not then create it
		try:
			profs = Professor.objects.get(first_name=prof[0], last_name=prof[1])
			profs.addCourse(newCourse)
			profs.save()
		except:
			newProf = Professor(first_name=prof[0],last_name=prof[1],subject=subject)
			newProf.save()
			newProf.addCourse(newCourse)
			newProf.save()

		return HttpResponseRedirect('/viewcourse/'+courseId)

def viewCourse(request, course_id):
	try:
		theCourse = Course.objects.get(courseID = course_id)
		courseReviews = theCourse.review_set.order_by('date')
		courseReviews = courseReviews.reverse()
		#courseReviews = theCourse.review_set.all()

		# calculate average rating
		averageRating = 0
		for review in courseReviews:
			averageRating += review.rating
		averageRating = float(averageRating) / len(courseReviews) if len(courseReviews) > 0 else 0
			
		context = RequestContext(request, {
			'course' : theCourse,
			'professor' : theCourse.professor_set.all()[0],
			'reviews' : courseReviews,
			'numReviews' : len(courseReviews),
			'averageRating' : averageRating,
		})
		return render(request, 'core/coursetemplate.html', context)
	except:
		return HttpResponse('Oops, that course does not exist')

def addReviewForm(request, course_id):
	context = RequestContext(request, {
		'courseId' : course_id,	
	})
	return render(request, 'core/addreviewtemplate.html', context)

def submitReview(request, course_id):
	rating = request.POST['rating']
	text = request.POST['review']
        
	try: 
		theCourse = Course.objects.get(courseID = course_id)
		theReview = Review(text=text,rating=rating,author=request.user,course=theCourse)
		theReview.save()
		return HttpResponseRedirect('/viewcourse/'+course_id)
	except:
		return HttpResponse('Oops, that course does not exist')

def subjectView(reqest, subject):
	 
	if subject in Course.SUBJECTS:
		return HttpResponseRedirect('/viewsubject/'+subject)
        else:
		return HttpResponseRedirect('/')

