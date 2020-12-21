import json

from django.http import HttpResponseRedirect, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import publicuserlinks
 
class ShortenLink(View):
    '''
    Class Handler for shortening links
    '''

    def get(self, request, *args, **kwargs):
        return JsonResponse({"query":"response"})

    def post(self, request, *args, **kwargs):
        
        publiclink = publicuserlinks.PublicUserLinks()

        ''' parse request body '''

        respdata = []
        data = json.loads(request.body)

        publiclink.url = data.get('url')
        publiclink.type = data.get('type')

        objs = publiclink.geturls()
        print(objs)
        
        for o in objs:
            respdata.append(o)

        return JsonResponse(respdata, safe=False)