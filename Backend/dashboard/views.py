from accounts.forms import ExtraUserInfoForm
from accounts.models import ExtraUserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import HttpResponseRedirect, render


@login_required
# Create your views here.
def dashboard(request):
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    context ={
        'user_extra': user_extra
    }
    return render(request, 'dashboard/dashboard_home.html', context)


@login_required
def CreateUserInfo(request):
    context = {}
    if request.user.is_authenticated:
        form = ExtraUserInfoForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_info = request.user
            instance.save()
            return HttpResponseRedirect('/')

        context = {
            'form': form
        }
    return render(request, 'accounts/create_userInfo.html', context)
