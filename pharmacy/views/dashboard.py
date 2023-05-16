from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda user: user.groups.filter(name="supervisor").exists())
def dashboard(request):
    return render(request, 'dashboard.html')
