from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from . import models
from django.utils import timezone


def list_tweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="login")
def add_tweet(request):
    if request.POST:
        message = request.POST["message"]
        tweet = models.Tweet(username=request.user, message=message, timestamp=timezone.now())
        tweet.save()
        return redirect(reverse('tweetapp:listtweet'))
    return render(request, 'tweetapp/addtweet.html')

@login_required()
def delete_tweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:listtweet")



class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Kullanıcı başarılı bir şekilde kayıt olduktan sonra yönlendirilecek sayfa
        return render(request, 'registration/signup.html', {'form': form})
