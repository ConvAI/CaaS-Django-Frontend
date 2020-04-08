from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user.models import UserProfileInfo
from userpanel.models import Bot,Language,lang_names
from userpanel.forms import BotForm,LanguageForm
from django.http.response import Http404
from main_site.settings import BOT_SERVER,BOT_SERVER_PORT

# Create your views here.
@login_required
def panel(request):
    userinfo = UserProfileInfo.objects.get(user=request.user)
    bots = Bot.objects.filter(user=request.user,c_info=userinfo)
    rows = 0
    count = bots.count()
    if(count):
        if(count%3==0):
            rows = bots.count()//3
        else:
            rows = bots.count()//3 + 1
    return render(request,'dashboard.html',context={'userinfo':userinfo,'bots':bots,'rows':range(rows)})

@login_required
def createBot(request):
    userinfo = UserProfileInfo.objects.get(user=request.user)
    if(request.method == 'GET'):
        return render(request,'createBot.html',context={'userinfo':userinfo})
    elif(request.method == 'POST'):
        botform = BotForm(data=request.POST)
        # langform = LanguageForm(data=request.POST)
        if(botform.is_valid()):
            # get lang name from key
            # TODO find a way to insert lang data upon database creation 
            # This logic is temporary
            # lang_inst = langform.save(commit=False)
            # lang_inst.lang_name = lang_names.get(request.POST.get('lang_code'),'en-us')
            # lang_inst.save()

            # new logic 
            lang_inst = Language.objects.get(lang_code=request.POST.get('lang_code'))

            bot_inst = botform.save(commit=False)
            bot_inst.c_info = userinfo
            bot_inst.user = userinfo.user
            bot_inst.lang = lang_inst
            bot_inst.save()
            return HttpResponseRedirect(reverse('user:userpanel:editBot',args=[bot_inst.id]))
        else:
            print(botform.errors)
        
        # TODO send errors to user to update form values
        # return render(request,'dashboard.html',context={'userinfo':userinfo})

    
@login_required
def editBot(request,bot_id):
    try:
        bot_inst = get_object_or_404(Bot, pk=bot_id)
    except Bot.DoesNotExist:
        raise Http404("Bot does not exist")
    
    userinfo = UserProfileInfo.objects.get(user=request.user)
    if(request.method == 'POST'):
        test = False
        if(request.POST.get('bot_paragraph')):
            bot_inst.paragraph = request.POST.get('bot_paragraph')
            bot_inst.is_deployed = False
            bot_inst.save()
            test = True
            bot_api_url = 'http://' + BOT_SERVER + ':' + BOT_SERVER_PORT
            return render(request,'editBot.html',{'bot':bot_inst,'userinfo':userinfo,'test':test,'bot_url':bot_api_url})
        else:
            bot_inst.paragraph = request.POST.get('bot_paragraph')
            bot_inst.is_deployed = False
            bot_inst.save()
    return render(request,'editBot.html',{'bot':bot_inst,'userinfo':userinfo,'test':False})

@login_required
def deploy(request):
    userinfo = UserProfileInfo.objects.get(user=request.user)
    bots = Bot.objects.filter(user=request.user,c_info=userinfo,paragraph__isnull=False)
    rows = 0
    count = bots.count()
    if(count):
        if(count%3==0):
            rows = bots.count()//3
        else:
            rows = bots.count()//3 + 1
    return render(request,'deploy.html',context={'userinfo':userinfo,'bots':bots,'rows':range(rows)})


@login_required
def deployBot(request,bot_id):
    try:
        bot_inst = get_object_or_404(Bot, pk=bot_id)
    except Bot.DoesNotExist:
        raise Http404("Bot does not exist")

    userinfo = UserProfileInfo.objects.get(user=request.user)
    if(request.method == 'POST'):
        bot_inst.is_deployed = True
        bot_inst.save()
        bot_api_url = 'http://' + BOT_SERVER + ':' + BOT_SERVER_PORT
        return render(request,'showScript.html',{'bot':bot_inst,'bot_url':bot_api_url,'userinfo':userinfo})
    elif(request.method == 'GET' and bot_inst.is_deployed):
        bot_api_url = 'http://' + BOT_SERVER + ':' + BOT_SERVER_PORT
        return render(request,'showScript.html',{'bot':bot_inst,'bot_url':bot_api_url,'userinfo':userinfo})


        
@login_required
def disableBot(request,bot_id):
    try:
        bot_inst = get_object_or_404(Bot, pk=bot_id)
    except Bot.DoesNotExist:
        raise Http404("Bot does not exist")

    userinfo = UserProfileInfo.objects.get(user=request.user)
    if(request.method == 'POST'):
        bot_inst.is_deployed = False
        bot_inst.save()
        return HttpResponseRedirect(reverse('user:userpanel:deploy'))