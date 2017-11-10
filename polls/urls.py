from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.IndexView.as_view(), name='vote'),
    url(r'^create/$', views.CreateQuestionView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateQuestionView.as_view(), name='editquestion'),
]
