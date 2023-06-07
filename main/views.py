from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView
import transliterate
from django.contrib import auth
from .models import *
from .forms import QuestionForm, LoginForm, SignUpForm, NewsForm


def index(request):
    dictionaries = Dictionary.objects.all().order_by('word')[:3]
    news = News.objects.all()[:3]
    context = {'title': 'Surdo', 'dictionaries': dictionaries, 'news': news}
    return render(request, 'main/index.html', context)


# admin
# zhasulan
def about_us(request):
    context = {'title': 'Жүйе туралы'}
    return render(request, 'main/about-us.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)

            form.save()
            return redirect('contact')
    form = QuestionForm()
    context = {'title': 'Байланыс', 'form': form}
    return render(request, 'main/contact-us.html', context)


class Search(ListView):
    template_name = 'main/search.html'

    def get_queryset(self):
        return Dictionary.objects.filter(word__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Іздеу'
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class Sort(ListView):
    template_name = 'main/search.html'

    def get_queryset(self):
        return Dictionary.objects.filter(word__startswith=self.request.GET.get("sort"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Сұрыптау'
        context["sort"] = f'sort={self.request.GET.get("sort")}&'
        return context


def news(request):
    news = News.objects.order_by('-created')
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    context = {'title': 'Жаңалықтар', 'news': pages}

    return render(request, 'main/news.html', context)


def news_detail(request, slug):
    new = get_object_or_404(News, slug=slug)
    context = {'title': new.title, 'new': new}

    return render(request, 'main/news-detail.html', context)


def word_detail(request, slug):
    word = get_object_or_404(Dictionary, slug=slug)
    context = {'title': word.word, 'word': word}

    return render(request, 'main/word-detail.html', context)


def signin(request):
    messages = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            try:
                auth.login(request, user)
            except:
                context = {'title': 'Кіру', 'form': form, 'messages': 'Логин немесе пароль қате!'}
                return render(request, 'main/signin.html', context)
            return redirect('home')
    else:
        form = LoginForm()
    context = {'title': 'Кіру', 'form': form, 'messages': messages}
    return render(request, 'main/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Users.objects.create(user=user,
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'],
                                 phone=form.cleaned_data['phone'],

                                 )
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'title': 'Тіркелу', 'form': form}
    return render(request, 'main/sign-up.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def addnews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, )

        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(transliterate.translit(form.title, reversed=True))
            form.save()

            return redirect('news')

    form = NewsForm()
    context = {'title': 'Жаңалықтар қосу', 'form': form}
    return render(request, 'main/addnews.html', context)


def questions(request):
    ques = QuesModel.objects.order_by('?')[:10]
    if request.method == 'POST':
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in ques:
            total += 1
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        user = Users.objects.get(user=request.user)
        Result.objects.create(user=user, score=score, percent=percent, correct=correct, incorrect=wrong, total=total)
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'main/result.html', context)

    context = {
        'questions': ques
    }
    return render(request, 'main/questions.html', context)

