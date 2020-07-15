from django.shortcuts import render
from footBallApp.forms import UserForm,UserProfileInfoForm, TeamForm, TeamMemberForm, MatchSchedulingForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    """
    Home page view
    """
    teams_obj = Teams.objects.all()
    Full_list = []
    teams_list = []
    for teams in teams_obj:
        team_dict = {}
        team_dict.update({'team':teams.team_name, 'coach':teams.coach, 'manager':teams.manager})
        team_member_obj = TeamMembers.objects.filter(team=teams)
        for each in team_member_obj:
            data = {}
            data.update({'name':each, 'age':each.age, 'position':each.position})
            teams_list.append(data)
        team_dict.update({'members':teams_list})
        teams_list = []
        Full_list.append(team_dict)
    return render(request,'footBallApp/index.html',{'team':Full_list})
    
@login_required
def special(request):
    """
    Method to obtain the response
    """
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    """
    Logout method
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """
    To create a superuser such as Admin, Manager. They have the provision to view
    and add teams, teamplayers, assigning match schedules.
    """
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'footBallApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    """
    Login function in which the admin or the manager can login to the platform
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('index'))
                user_form = UserForm()
                profile_form = UserProfileInfoForm()
                teams_obj = Teams.objects.all()
                Full_list = []
                teams_list = []
                for teams in teams_obj:
                    team_dict = {}
                    team_dict.update({'team':teams.team_name, 'coach':teams.coach, 'manager':teams.manager})
                    team_member_obj = TeamMembers.objects.filter(team=teams)
                    for each in team_member_obj:
                        data = {}
                        data.update({'name':each, 'age':each.age, 'position':each.position})
                        teams_list.append(data)
                    team_dict.update({'members':teams_list})
                    teams_list = []
                    Full_list.append(team_dict)
                return render(request,'footBallApp/index.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'team':Full_list
                           })
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'footBallApp/login.html', {})

def addTeam(request):
    """
    Add a new team with a coach and manager
    """
    registered = False
    if request.method == 'POST':
        team_form = TeamForm(data=request.POST)
        if team_form.is_valid():
            team = team_form.save()
            registered = True
        else:
            print(team_form.errors)
    else:
        team_form = TeamForm()
    return render(request,'footBallApp/team.html',
                          {'team_form':team_form,
                           'registered':registered})

def addTeamMember(request):
    """
    Add new team members to the previously added teams
    """
    registered = False
    if request.method == 'POST':
        team_member_form = TeamMemberForm(data=request.POST)
        if team_member_form.is_valid():
            team_member = team_member_form.save()
            registered = True
        else:
            print(team_member_form.errors)
    else:
        team_member_form = TeamMemberForm()
    return render(request,'footBallApp/team_member.html',
                          {'team_member_form':team_member_form,
                           'registered':registered})

def matchScheduling(request):
    """
    Assigning match schedules, Adding results when the match once completed
    """ 
    registered = False
    if request.method == 'POST':
        scheduling_form = MatchSchedulingForm(data=request.POST)
        if scheduling_form.is_valid():
            scheduling = scheduling_form.save()
            registered = True
        else:
            print(scheduling_form.errors)
    else:
        scheduling_form = MatchSchedulingForm()
    matches_obj = MatchScheduling.objects.all()
    return render(request,'footBallApp/match_scheduling.html',
                          {'scheduling_form':scheduling_form,
                           'registered':registered, 'matches_obj':matches_obj})