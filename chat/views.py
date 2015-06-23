from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, 'chat/index.html')


def about(request):
    return render(request, 'chat/about.html')


@login_required
def roster(request):
    roster_list = User.objects.order_by('username')
    context_dict = {'members': roster_list}
    return render(request, 'chat/roster.html', context_dict)
