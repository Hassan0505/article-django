from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('register/', views.register, name='register'),
    path('home/',views.HomeItemClass.as_view(), name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('pay/<int:article_id>/', views.pay, name='pay'),
]