from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('search/', views.Search.as_view(), name='search'),
    path('sort/', views.Sort.as_view(), name='sort'),
    path('news/', views.news, name='news'),
    path('news/addnews/', views.addnews, name='addnews'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('words/<slug:slug>/', views.word_detail, name='word_detail'),
    path('account/signin/', views.signin, name='account_signin'),
    path('account/signup/', views.signup, name='account_signup'),
    path('account/logout/', views.logout, name='account_logout'),
    path('questions/', views.questions, name='questions'),
]
