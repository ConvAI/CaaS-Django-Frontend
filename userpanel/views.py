from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user.models import UserProfileInfo
# Create your views here.
@login_required
def panel(request):
    userinfo = UserProfileInfo.objects.get(user=request.user)
    return render(request,'dashboard.html',context={'userinfo':userinfo})