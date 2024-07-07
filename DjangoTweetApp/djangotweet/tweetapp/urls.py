from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',  views.list_tweet, name="listtweet"),  # asd.com/tweetapp/
    path('addtweet/', views.add_tweet, name="addtweet"),  # asd.com/tweetapp/addtweet
    path('signup/', views.SignUpView.as_view(), name="signup"),  # asd.com/tweetapp/addtweet
    path('deletetweet/<int:id>', views.delete_tweet, name="deletetweet"),  # asd.com/tweetapp/addtweet

]