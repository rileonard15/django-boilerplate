from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.FrontPage.as_view(), name='login'),
    url(r'^logout/', views.LogoutHandler.as_view(), name='logout'),
]