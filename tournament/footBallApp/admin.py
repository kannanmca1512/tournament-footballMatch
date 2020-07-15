from django.contrib import admin
from .models import UserProfileInfo, Teams, TeamMembers, MatchScheduling

admin.site.register(UserProfileInfo)
admin.site.register(Teams)
admin.site.register(TeamMembers)
admin.site.register(MatchScheduling)