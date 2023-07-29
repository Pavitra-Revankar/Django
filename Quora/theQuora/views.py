from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect,request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView
from .forms import AnswerForm
from .models import Question, Answer


def SignUpPage_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        if password != re_password:
            return HttpResponse("Your password doesn't match")
        else:
            my_users = User.objects.create_user(username, email, password)
            my_users.save()
            # return HttpResponse("Successfully created an account!")
            return redirect('login')
    return render(request, 'Signup.html')


def LogInPage_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('page')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'Login.html')


class QuoraPageView(ListView):
    model = Question
    template_name = 'QuoraPage.html'


class AskQuestion(CreateView):
    model = Question
    template_name = 'AskQuestion.html'
    fields = [
        'question',
        'user'
    ]

    # success_url = reverse_lazy('page')


class Questions(DetailView):
    model = Question
    template_name = 'Question.html'
    context_object_name = 'q'



    # def get_context_data(self, *args, **kwargs):
    #     # answer_model = Answer.objects.all()
    #     context = super(Questions, self).get_context_data(*args, **kwargs)
    #     # p = request.POST.get('answer_id')
    #     stuff = get_object_or_404(Question, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #     context["total_likes"] = total_likes


class AnswerView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'Answer.html'

    def form_valid(self, form):
        form.instance.Questions_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
       return reverse('question',kwargs={'pk':self.kwargs['pk']})

    # success_url = reverse_lazy('page')


def LikeView(request,pk):
    # ans = Question.objects.get(id=pk)
    ans = get_object_or_404(Question,id=pk)
    if ans.likes.filter(id=request.user.id):
        ans.likes.remove(request.user)
    else:
        ans.likes.add(request.user)
    return HttpResponseRedirect(reverse('question', args=[str(pk)]))