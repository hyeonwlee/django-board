from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def answer_comment_create(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#answer_{}'.format(resolve_url(
                'pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = CommentForm()
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/question_detail.html', context)