from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def roster(request):
    roster_list = User.objects.order_by('username')
    context_dict = {'members': roster_list}
    return render(request, 'userprofile/roster.html', context_dict)
