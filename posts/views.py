from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader
import requests


# Create your views here.


def posts_list(request):
	data = requests.get('https://zackio.herokuapp.com/posts').json()
	template = loader.get_template('posts.html')
	context = {"data": data}
	return HttpResponse(template.render(context,request))