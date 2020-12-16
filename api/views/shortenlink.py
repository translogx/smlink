import json

from django.http import HttpResponseRedirect, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View

class ShortenLink(View):
    '''
    Class Handler for shortening links
    '''

    def get(self, request, *args, **kwargs):
        return JsonResponse({"query":"response"})

    def post(self, request, *args, **kwargs):
        print(str(json.loads(request.body)))
        #print(request.META)
        return JsonResponse({"request.body()":"ghj"})