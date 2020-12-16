from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View

class RealLink(View):

    def post(self, request, urlref, *args, **kwargs):
        print(request.body)
        print(urlref)
        return JsonResponse({"request.body()":"ghj"})

    