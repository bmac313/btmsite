from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	template = loader.get_template("polls/index.html")
	context = {
		"latest_question_list": latest_question_list,
	}
	return render(request, "polls/index.html", context)
	# above is equivalent to:
	# return HttpResponse(template.render(context, request))

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})
	#above is equivalent to:
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#	
	#return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
	return HttpResponse("Viewing results for questions %s." % question_id)

def vote(request, question_id):
	return HttpResponse("Voting on question %s." % question_id)
