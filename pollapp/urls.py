from django.conf.urls import url

from . import views

app_name = "pollapp"
urlpatterns = [
    # ex: /pollapp/
    url(r'^$', views.index, name='index'),
    # ex: /pollapp/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /pollapp/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /pollapp/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]