from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

##############################
#User routes
##############################
user_urlpatterns = [
    url(r'^register/', views.RegisterView.as_view(), name='register-view'),
    url(r'^bill/(?P<pk>[\w-]+)/$', views.BillView.as_view(), name='bill-view'),
    url(r'^current-bill/', views.CurrentBill.as_view(), name='current-bill'),
    url(r'^notifications/', views.Notifications.as_view(), name='user-notifications'),
    url(r'^bills/', views.ViewBills.as_view(), name='bill-views'), 
    url(r'^charges/(?P<title>[\w-]+)/$', views.AddCharge.as_view(), name='add-charge'),
    url(r'^property/(?P<pk>[\w-]+)/$', views.UserProperty.as_view(), name='property-user'),
    url(r'^bill-user/(?P<pk>[\w-]+)/$', views.BillUser.as_view(), name='bill-user'),

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
    url(r'^property-size/', include(property_urlpatterns)),

    #url(r'^notifications/', include(song_urlpatterns)),
]


urlpatterns = format_suffix_patterns(urlpatterns)
