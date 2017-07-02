from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.JSONResponse.snippet_list),
    url(r'^/(?P<pk>\d+)$', views.JSONResponse.snippet_detail),
]
