from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.index_view, name='index'),
    path('get-categories/', views.get_categories, name='get_categories'),
    path('search/', views.search_users, name='search_users'),
    path('logout/', views.logout_view, name='logout'), 
]
