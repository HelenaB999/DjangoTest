from django.core.checks import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse


# Create your views here.
def index(request):
    http_response = HttpResponse()
    http_response.write('<html> HW. </html>')
    return http_response
