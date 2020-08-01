from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

##############################
#User routes
##############################
user_urlpatterns = [
    url(r'^register/', views.RegisterView.as_view(), name='register-view'),

]

property_urlpatterns = [
    url(r'^county-lots/(?P<title>[\w-]+)/$', views.LotSizeCounty.as_view(), name='county-lots-view'),
    url(r'^county-tiers/(?P<title>[\w-]+)/$', views.LotSizeTiers.as_view(), name='county-lots-tiers'),
    url(r'^county-service-charges/(?P<title>[\w-]+)/$', views.CountyCharges.as_view(), name='county-service-charges'),
]


########################################
#Everything related to the state model
########################################






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
    url(r'^property-size/', include(user_urlpatterns)),

    #url(r'^notifications/', include(song_urlpatterns)),
]


urlpatterns = format_suffix_patterns(urlpatterns)
