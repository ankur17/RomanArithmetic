from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def basic(request):
#     return render(request,'basic.html')

# def basic(request):
# 	t = loader.get_template('myanswer/basic.html')
	
# 	return HttpResponse(t.render(request))
# 	# return HttpResponse("<h1>This is the ans</h1>")

def homePage(request):
    return render(request,'home/home.html')
