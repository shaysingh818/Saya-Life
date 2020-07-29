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
state_urlpatterns = [
    url(r'^states/', views.StatesView.as_view(), name='states-view'),
    url(r'^state/(?P<pk>[\w-]+)/$', views.StateView.as_view(), name='state-detail'),
]



########################################
#Everything related to the County model
########################################
county_urlpatterns = [
    url(r'^counties/', views.CountiesView.as_view(), name='counties-view'),
    url(r'^county/(?P<pk>[\w-]+)/$', views.CountyView.as_view(), name='county-detail'),
    url(r'^county-state/(?P<pk>[\w-]+)/$', views.CountyStateView.as_view(), name='county-state-view'),
    url(r'^county-lots/(?P<pk>[\w-]+)/$', views.LotSizeCounty.as_view(), name='county-lots-view'),
    url(r'^county-tiers/(?P<pk>[\w-]+)/$', views.LotSizeTiers.as_view(), name='county-lots-tiers'),

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
    url(r'^states/', include(state_urlpatterns)),
    url(r'^counties/', include(county_urlpatterns)),
    #url(r'^notifications/', include(song_urlpatterns)),
]


urlpatterns = format_suffix_patterns(urlpatterns)
