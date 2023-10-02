from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:num>/", views.number_view, name="num_view"),
    path("<str:item>/",views.course_view, name="course"),
    path("<int:num1>/<int:num2>/", views.multiply, name="multiply"),
    

]