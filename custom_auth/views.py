import requests, json
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


# Create your views here.

def login(request):
    return render(request, 'login.html')


@login_required(login_url='login/')
def index(request):
    user = UserSocialAuth.objects.get(user=request.user)
    r = requests.get('https://api.vk.com/method/friends.get',
                     params={'user_ids': 41, 'access_token': user.access_token, 'v': '5.120',
                             'fields': ['nickname', 'sex', 'photo_50'], 'count': 5})
    friends = json.loads(r.text)
    return render(request, 'index.html', context={"user": " ".join([request.user.first_name, request.user.last_name]),
                                                  'friends': friends['response']['items']})


@login_required(login_url='login/')
def logout(request):
    auth_logout(request)
    return redirect('login')
