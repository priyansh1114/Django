from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   peoples = [
      {'name':'Priyanshu','age':25,},
      {'name':'Himashu','age':26, },
      {'name':'Golu','age':10,}
   ]
   return render(request , "index.html", context = {'peoples':peoples})

def about(request):
   return render (request,"about.html")

def contact(request):
   context = {'page': 'about'}
   return render (request,"contact.html",context)