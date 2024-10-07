from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib import messages
from .models import Article, Payment
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def hello(request):
    return render(request, 'hello.html')

# def home(request):
#     return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            User.objects.create_user(clean_data['username'], clean_data['email'], clean_data['password'])
            messages.success(request, 'user registered successfully', 'success')
            return redirect('home')
    else:
        form = UserRegisterationForm()

    return render(request, 'register.html', {'form': form})    

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username = clean_data['username'], password = clean_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'{user} logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

class HomeItemClass(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   
        
        context.update({
            'articles': Article.objects.all(),
        })

        return context
    
def detail(request, id):
    content = Article.objects.get(pk=id)
    return render(request, 'detail.html', {'content':content})


def pay(request, article_id):
    content = Article.objects.get(id=article_id)
    if not request.user.is_authenticated:
        messages.error(request, 'you have to singeup', 'danger')
        redirect('home')
    else:
        try:
            Payment.objects.get(article=content, user=request.user)
            return render(request, 'detail.html', {'content':content})
         
        except:            
            Payment.objects.create(article=content, user=request.user)
            messages.success(request, 'your payment is seccessfully', 'seccess')
            return render(request, 'detail.html', {'content':content})
            



