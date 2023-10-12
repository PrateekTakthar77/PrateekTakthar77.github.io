from django.shortcuts import render, HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("this is the 'home' page of bakul's new and cool website which is currently under development")
def index(request):
    return render(request, "index.html")


def about_me(request):
    return HttpResponse("this is the 'about' me page of bakul's new and cool website which is currently under development")


def blog(request):
    return HttpResponse("this is the 'blog' page of bakul's new and cool website which is currently under development")


def contact_me(request):
    return HttpResponse("this is the 'contact me' page of bakul's new and cool website which is currently under development")


def projects(request):
    return HttpResponse("this is the 'projects' page of bakul's new and cool website which is currently under development")
