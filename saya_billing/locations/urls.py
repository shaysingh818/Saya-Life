from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


geographic_urlpatterns = [
    url(r'^states/', views.StatesView.as_view(), name='states-view'),
    url(r'^state/(?P<pk>[\w-]+)/$', views.StateView.as_view(), name='state-detail'),
    url(r'^counties/', views.CountiesView.as_view(), name='counties-view'),
    url(r'^county/(?P<pk>[\w-]+)/$', views.CountyView.as_view(), name='county-detail'),
    url(r'^state-counties/(?P<code>[\w-]+)/$', views.CountyStateView.as_view(), name='county-state-view'),

]


search_urlpatterns = [
    url(r'^states/$', views.StateSearch.as_view(), name='states-search'),
    url(r'^counties/$', views.CountySearch.as_view(), name='county-search'),

]


####################
# Application URLs #
####################
urlpatterns = [
    url(r'^geo/', include(geographic_urlpatterns)),
    url(r'^search/', include(search_urlpatterns)),

    #url(r'^notifications/', include(song_urlpatterns)),
]



urlpatterns = format_suffix_patterns(urlpatterns)
