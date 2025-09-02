from django.http import HttpResponse
from django.shortcuts import render


def home(requst):
    # return HttpResponse("Hello, world . you are at chai aur Django home page")
    return render(requst,'website/index.html')
def about(requst):
    return HttpResponse("Hello, world . you are at chai aur Django about page")
def contact(requst):
    return HttpResponse("Hello, world . you are at chai aur Django contact page")