from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from django.shortcuts import render

# Create your views here.

def logout_view(request):
	"""注销用户"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
