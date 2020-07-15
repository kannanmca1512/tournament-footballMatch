from django.conf.urls import url
from footBallApp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# SET THE NAMESPACE!
app_name = 'footBallApp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('addTeam/', views.addTeam, name='addTeam'),
    path('addTeamMember/', views.addTeamMember, name='addTeamMember'),   
    path('matchScheduling/', views.matchScheduling, name='matchScheduling'),   
]
