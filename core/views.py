from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib
from core.utils.network import get_domain
from django.conf import settings
from django.contrib import auth
from core.decorators import ajax_endpoint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from core.utils.facebook import get_facebook_friend_data


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def facebook_login(request):
    login_link = 'https://www.facebook.com/dialog/oauth?' + urllib.urlencode(
        {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': get_domain(request) + '/',
            'response_type': 'code',
            'scope': 'email',
            'state': 'facebook',
        }
    )
    return HttpResponseRedirect(login_link)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@csrf_exempt
@login_required
@ajax_endpoint
def api_friend_list(request):
    access_token = request.session['facebook_access_token']
    response = {}
    response['friend_list'] = get_facebook_friend_data(access_token)['data']
    return response, 200
