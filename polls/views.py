from .models import Choice, Question

from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.views import generic

from polls.forms.createquestion_form import CreateQuestionForm
from polls.forms.updatequestion_form import UpdateQuestionForm
from polls.forms.createchoice_form import CreateChoiceForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:50]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    '''
    def vote(request, question_id):
        p = get_object_or_404(Question, pk=question_id)

        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
            return HttpResponseRedirect('Results view')'''


class CreateQuestionView(generic.CreateView):
    model = Question
    template_name = 'polls/createquestion.html'
    form_class = CreateQuestionForm

    def post(self, request, *args, **kwargs):
        self.object = None
        context = super(
            CreateQuestionView, self).post(request, *args, **kwargs)
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        # i = request.POST['question_text']
        form = self.get_form()
        if form.is_valid():
            entry = request.POST['question_text']
            existing = Question.objects.filter(question_text=entry).exists()

            if existing:
                return self.form_invalid(form=form, error=1)
            else:
                q = Question.objects.create(
                    question_text=entry, pub_date=timezone.now())
                q.save()
                return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        return HttpResponseRedirect(reverse('polls:index'))

    def form_invalid(self, form, error):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        if error == 1:
            return self.render_to_response(self.get_context_data(
                form=form, error_message="Existing entry"))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UpdateQuestionView(generic.UpdateView):
    model = Question
    template_name = 'polls/updatequestion.html'
    form_class = UpdateQuestionForm

    def post(self, request, *args, **kwargs):
        self.object = None
        context = super(
            UpdateQuestionView, self).post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            entry = request.POST['question_text']
            existing = Question.objects.filter(question_text=entry).exists()

            if existing:
                return self.form_invalid(form=form, error=1)
            else:
                q = Question.objects.get(pk=request.POST['id'])
                q.question_text = entry
                q.pub_date = timezone.now()
                q.save()
                return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        return HttpResponseRedirect(reverse('polls:index'))

    def form_invalid(self, form, error):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        if error == 1:
            return self.render_to_response(self.get_context_data(
                form=form, error_message="Existing entry"))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CreateChoiceView(generic.CreateView):
    model = Question
    template_name = 'polls/createchoice.html'
    form_class = CreateChoiceForm
    success_url = reverse_lazy('polls:index')
