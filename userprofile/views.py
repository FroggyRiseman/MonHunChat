from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from userprofile.models import UserProfile

from forms import UserProfileForm

def roster(request):
    roster_list = User.objects.order_by('username')
    context_dict = {'members': roster_list}
    return render(request, 'userprofile/roster.html', context_dict)


@login_required
def update_profile(request):
    userProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(initial={'description': userProfile.description})
    return render_to_response(
            'userprofile/update_profile.html',
            {'form': form},
            RequestContext(request)
    )
