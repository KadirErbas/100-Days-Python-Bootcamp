from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


course_dic={
    "python":"this is python course",
    "java":"this is java course",
    "kuzikeri": "this is kuzikeri course",
    
}
def index(request):
    return HttpResponse("index")

def course_view(request, item):
    try:
        return HttpResponse(course_dic[item])
    except:
        return HttpResponseNotFound("Not found! Please look for another course!")
        #raise Http404("wtf")
    #return HttpResponse(course_dic.get(item,"oyle bi sey yok tamam mı"))

def multiply(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1*num2}")

def number_view(request, num):
    try:
        course_list = list(course_dic.keys())
        course = course_list[num]
        return HttpResponseRedirect(reverse("course", args=[course]))
    except:
        return HttpResponseNotFound("Not found! Please look for another course!")