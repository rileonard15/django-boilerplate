from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.template import loader, RequestContext
from django.http import HttpResponse
from rest_framework import status


import urllib2
import urllib
import json

class BaseHandler(APIView):
    def __init__(self, request=None, response=None):
        self.tv = {}
        self.request = request

    def render(self, request, template_path):
        if "error" in request.session:
            self.tv["error"] = request.session["error"]

        template = loader.get_template(template_path)
        return HttpResponse(template.render(RequestContext(request, self.tv)))

    def api_response(self, status_code, response):
        
        if status_code == 200:
            return Response(response, status=status.HTTP_200_OK)
        elif status_code == 201:
            return Response(response, status=status.HTTP_201_CREATED)
        elif status_code == 400:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        elif status_code == 401:
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        elif status_code == 403:
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        elif status_code == 404:
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        elif status_code == 405:
            return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        elif status_code == 408:
            return Response(response, status=status.HTTP_408_REQUEST_TIMEOUT)

    def api_read_response(self, req):
        try:
            response = urllib2.urlopen(req)
            result = json.loads(response.read())
            return result['status_code'], result['response']
        except urllib2.HTTPError, e:
            result = json.loads(e.read())
            print result
            return e.code, result