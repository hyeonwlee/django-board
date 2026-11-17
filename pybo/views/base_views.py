from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question, Answer, Comment

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj, 
        'page': page, 
        'kw': kw
    }
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # 답변 정렬
    sort = request.GET.get('sort', 'date')
    if sort == 'voter':
        answer_list= question.answer_set.order_by('-voter','-create_date')
    else:
        answer_list = question.answer_set.order_by('-create_date')
    
    # 답변 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(answer_list, 5)
    page_obj = paginator.get_page(page)

    context = {
        'question': question,
        'answer_list': page_obj,
        'sort': sort,
    }

    return render(request, 'pybo/question_detail.html', context)
