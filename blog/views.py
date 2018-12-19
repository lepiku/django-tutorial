from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def homepage(request):
	return render(request, 'homepage.html')

def index(request):
	#return HttpResponse("Hello world! You're at blog index")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
			'latest_question_list': latest_question_list,
			}

	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
	return HttpResponse("You're looking at results of question {}".format(
			question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question {}".format(question_id))
