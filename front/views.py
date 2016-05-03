import base64
import urllib2
import urllib
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect

from main.base import BaseHandler
from main import helpers as h

from django.contrib.auth.models import User


class FrontPage(BaseHandler):
    def get(self, request):
        if self.request.user.is_authenticated():
            return redirect("/dashboard/")

        self.tv["current_page"] = "frontpage"
        return self.render(request, 'front/index.html')


    def post(self, request):
        email = self.request.data["email"]
        password = self.request.data["password"]

        if h.EMAIL_REGEX.match(email):
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                request.session["error"] = 'Email does not exist..'
                request.session.set_expiry(10)
                return redirect("/")
        else:
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                request.session["error"] = 'Email does not exist..'
                request.session.set_expiry(10)
                return redirect("/")

        if user.is_active == False:
            request.session["error"] = 'Email does not exist..'
            request.session.set_expiry(10)
            return redirect("/")


        if user.check_password(password):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect("/dashboard/")
        else:
            request.session["error"] = 'Email and Password does not match..'
            request.session.set_expiry(10)
            return redirect("/")

class LogoutHandler(BaseHandler):
    def get(self, request):
        logout(request)
        return redirect("/")



