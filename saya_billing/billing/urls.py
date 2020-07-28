from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

##############################
#User routes
##############################
user_urlpatterns = [
    url(r'^register/', views.RegisterView.as_view(), name='register-view'),

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
    #url(r'^notifications/', include(song_urlpatterns)),
]


urlpatterns = format_suffix_patterns(urlpatterns)