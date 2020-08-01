from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^states/', views.StatesView.as_view(), name='states-view'),
    url(r'^state/(?P<pk>[\w-]+)/$', views.StateView.as_view(), name='state-detail'),
    url(r'^counties/', views.CountiesView.as_view(), name='counties-view'),
    url(r'^county/(?P<pk>[\w-]+)/$', views.CountyView.as_view(), name='county-detail'),
    url(r'^state-counties/(?P<code>[\w-]+)/$', views.CountyStateView.as_view(), name='county-state-view'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
