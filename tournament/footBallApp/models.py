
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    """
    Additional informations aparts from the default user model
    """
    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (4, 'manager'),
  )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    age = models.IntegerField(blank=True, null=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    def __str__(self):
        return self.user.username

class Teams(models.Model):
    """
    Model for creating a team
    """
    team_name = models.CharField(max_length = 200, unique=True)
    coach = models.CharField(max_length = 200)
    manager = models.CharField(max_length = 200)
    def __str__(self):
        return self.team_name

class TeamMembers(models.Model):
    """
    Model for creating a team member
    """
    team = models.ForeignKey(Teams,related_name="team",on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class MatchScheduling(models.Model):
    """
    Time Scheduling of the team battles
    """
    MATCH_STATUS = (
      (1, 'upcoming'),
      (2, 'inprogress'),
      (3, 'completed'),
  )
    first_team = models.ForeignKey(Teams,related_name="team1",on_delete=models.CASCADE)
    second_team = models.ForeignKey(Teams,related_name="team2",on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    match_status = models.PositiveSmallIntegerField(choices=MATCH_STATUS, default=1)
    result = models.CharField(max_length = 200, null=True, blank=True)
    def __str__(self):
        return self.first_team.team_name+" Vs "+self.second_team.team_name

