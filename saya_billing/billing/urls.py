from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

##############################
#User routes
##############################
user_urlpatterns = [
    url(r'^register/', views.RegisterView.as_view(), name='register-view'),

]


########################################
#Everything related to the state model
########################################
locations_urlpatterns = [
    url(r'^states/', views.StatesView.as_view(), name='states-view'),
    url(r'^state/(?P<pk>[\w-]+)/$', views.StateView.as_view(), name='state-detail'),
    url(r'^counties/', views.CountiesView.as_view(), name='counties-view'),
    url(r'^county/(?P<pk>[\w-]+)/$', views.CountyView.as_view(), name='county-detail'),
    url(r'^state-counties/(?P<code>[\w-]+)/$', views.CountyStateView.as_view(), name='county-state-view'),
    url(r'^county-lots/(?P<title>[\w-]+)/$', views.LotSizeCounty.as_view(), name='county-lots-view'),
    url(r'^county-tiers/(?P<title>[\w-]+)/$', views.LotSizeTiers.as_view(), name='county-lots-tiers'),
    url(r'^county-service-charges/(?P<title>[\w-]+)/$', views.CountyCharges.as_view(), name='county-service-charges'),
]






##############################
#Device song routes
##############################
#messages_urlpatterns = [

    #url(r'^search/$', views.SongSearch.as_view(), name='songs-search'),
#]



####################
# Application URLs #
####################
urlpatterns = [
    url(r'^users/', include(user_urlpatterns)),
    url(r'^locations/', include(locations_urlpatterns)),
    #url(r'^notifications/', include(song_urlpatterns)),
]


urlpatterns = format_suffix_patterns(urlpatterns)
