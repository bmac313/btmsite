from django.db.models import F as field  # Alias 'F' so code is easier to read.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"
	def get_queryset(self):
		"""
		Return the last 5 published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = "polls/detail.html"
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = "polls/results.html"
	

def vote(request, question_id): # TODO: POST views should be called [x]Action (ex: VoteAction) for consistency
	question = get_object_or_404(Question, pk=question_id)
	try:
		# get the 'choice' record with primary key (pk) equal to the ID provided by POST.
		selected_choice = question.choice_set.get(pk=request.POST["choice"])
	except (KeyError, Choice.DoesNotExist):
		# Re-display the question voting form.
		return render(
			request,
			"polls/detail.html",
			{
				"question": question,
				"error_message": "You didn't select a choice!",
			},
		)
	else:
		# Increment the vote count by 1.
		selected_choice.votes = field("votes") + 1
		selected_choice.save()
		
		# Always return an HttpResponseRedirect after successfully dealing with POST.
		# This prevents data from being posted twice if a user hits Back on the keyboard.
		return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
